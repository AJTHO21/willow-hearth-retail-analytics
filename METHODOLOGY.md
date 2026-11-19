# Methodology and reproduction scope

The full local engagement preserves the raw workbook, classifies each transaction, builds fact/dimensions, calculates KPIs, investigates exceptions and reconciles dashboard/report figures. Original rows and duplicate candidates remain traceable. The published subset includes a new read-only verifier rather than historical builders that write into fixed output folders or depend on local project structure.

## Included execution

`python scripts/verify_fact_kpis.py --fact /path/to/P001_fact_transactions.csv`

The script uses csv, Decimal, pathlib, argparse and other Python standard-library modules. It requires no third-party packages. It checks full-period and November financial/customer/order/product measures, source count, positive units, exact-SKU identity, and the complete four-row pair sensitivity. It prints aggregates and exits 1 on required failures. It does not mutate its input. Python 3.10+ is a compatibility target; the tested runtime and actual results are in QUALITY_ASSURANCE_SUMMARY.md. No requirements.txt is supplied because there are no external runtime dependencies.

## Not included

This reduced package does not rebuild the classified fact from the raw XLSX, reproduce the entire local QA suite, export a Power BI model, prove exact deployed key formulas or execute DAX/live visuals. Existing builders were reviewed for fixed-folder writes, dependencies and assumptions; no claim is made that they are safe portable drop-in commands. Classification/case-mapping decisions require the full documented project context. Power BI and Office/PDF tools are needed for their respective live/rendered checks; no such execution is claimed by this verifier.

## Public package scope

The public package includes the [final portfolio case study PDF](assets/P001_Portfolio_Case_Study_FINAL.pdf), supporting documentation and the verifier. Transaction data, Power BI and client-handoff files, local manifests and environment folders remain outside the package. No secrets or private source paths are required by the new verifier.
