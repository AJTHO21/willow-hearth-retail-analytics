"""Read-only verification of a project-format processed fact CSV; stdlib only."""
import argparse
import csv
import json
import sys
from decimal import Decimal
from pathlib import Path

D = Decimal
PAIRS = {"541431", "C541433", "581483", "C581484"}
EXPECTED = {
    "full": ["10271433.063", "-478724.18", "9792708.883", 19773, 4334, 2829, 3908, 5577103, "8761066.653", "1510366.41"],
    "november": ["1457745.53", "-25010.54", "1432734.99", 2751, 1660, 534, 2934, 750082, "1142145.77", "315599.76"],
}

def population():
    return {"sales": D(0), "cancellations": D(0), "known": D(0), "orders": set(), "customers": {}, "products": set(), "units": 0}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fact", type=Path, required=True)
    args = parser.parse_args()
    groups = {"full": population(), "november": population()}
    count = 0
    pair_count = 0
    pair_positive = D(0)
    pair_negative = D(0)
    remaining_sku_sales = D(0)
    with args.fact.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        required = {"InvoiceNo", "CustomerID", "ProductKey", "Quantity", "LineValue", "InvoiceDate", "TransactionType", "ItemType"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("Required columns missing")
        for row in reader:
            count += 1
            invoice = row["InvoiceNo"]
            value = D(row["LineValue"])
            qualifying = row["ItemType"] == "Merchandise / unreviewed"
            sale = qualifying and row["TransactionType"] == "Candidate sale"
            cancel = qualifying and row["TransactionType"] == "Cancellation"
            if invoice in PAIRS:
                pair_count += 1
                if sale:
                    pair_positive += value
                elif cancel:
                    pair_negative += value
                else:
                    raise ValueError("Pair row outside defined sale/cancellation population")
            if sale and row["ProductKey"] == "23843" and invoice not in PAIRS:
                remaining_sku_sales += value
            for name in ["full"] + (["november"] if row["InvoiceDate"].startswith("2011-11") else []):
                group = groups[name]
                if cancel:
                    group["cancellations"] += value
                if sale:
                    group["sales"] += value
                    group["orders"].add(invoice)
                    group["products"].add(row["ProductKey"])
                    group["units"] += int(row["Quantity"])
                    customer = row["CustomerID"]
                    if customer.strip():
                        group["known"] += value
                        group["customers"].setdefault(customer, set()).add(invoice)
    failures = []
    output = {}
    if count != 541909:
        failures.append("Record count")
    for name, group in groups.items():
        values = [group["sales"], group["cancellations"], group["sales"] + group["cancellations"], len(group["orders"]), len(group["customers"]), sum(len(v) >= 2 for v in group["customers"].values()), len(group["products"]), group["units"], group["known"], group["sales"] - group["known"]]
        for index, (actual, expected) in enumerate(zip(values, EXPECTED[name])):
            if abs(D(actual) - D(expected)) > D("0.000001"):
                failures.append(name + " benchmark " + str(index))
        output[name] = dict(zip(["sales", "cancellations", "after_cancellation", "orders", "identified", "repeat", "products", "units", "identified_sales", "unidentified_sales"], [str(v) for v in values]))
        output[name]["repeat_rate_percent"] = str(D(values[5]) * 100 / D(values[4]))
    if pair_count != 4 or pair_positive != D("245653.20") or pair_negative != -pair_positive or remaining_sku_sales != 0:
        failures.append("Four-row sensitivity boundary")
    output["sensitivity"] = {"excluded_rows": pair_count, "sales": str(groups["full"]["sales"] - pair_positive), "cancellations": str(groups["full"]["cancellations"] - pair_negative), "remaining_sku_23843_sales": str(remaining_sku_sales)}
    output["record_count"] = count
    output["failures"] = failures
    print(json.dumps(output, indent=2))
    return 1 if failures else 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, ArithmeticError, csv.Error) as error:
        print("Mandatory verification failed: " + str(error), file=sys.stderr)
        sys.exit(1)
