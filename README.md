# Willow & Hearth Retail | E-commerce analytics portfolio

Project 001 shows how a retailer can use transaction data to understand sales trends, customer purchasing and product performance, and see where unusual entries can change the picture. The project turned **541,909 original transaction records** into a **four-page Power BI dashboard** and management findings with recommendations, including where to improve customer ID capture and which large matching invoices to investigate.

Willow & Hearth Retail and Sarah Mitchell are fictional. This self-directed portfolio project uses public historical data and represents no paid engagement, real-client approval or actual commercial results. The simulated client engagement was completed and internally approved on November 17, 2026, under documented analytical limitations.

**[View the five-page portfolio case study (PDF)](assets/P001_Portfolio_Case_Study_FINAL.pdf)**

## What the analysis covers

- **Executive Overview and Sales Performance** track candidate merchandise sales, order volume and average order value across complete observed months.
- **Customer Analytics** examines observed repeat purchasing among identified customers and shows where a few accounts drive geographic sales totals.
- **Product Performance** compares rankings by sales value and units. A separate sensitivity analysis tests how two large matching positive and negative invoice pairs affect the rankings.

[Read the case study for findings and recommendations](PORTFOLIO_CASE_STUDY.md).

## Methodology and limitations

Python data preparation and quality assurance preserved the original records, classified transactions, flagged potential duplicates and reconciled sales, customer and product measures. [Methodology](METHODOLOGY.md) · [Reporting definitions](REPORTING_DEFINITIONS.md)

Candidate merchandise sales measure positive qualifying transaction value before cancellation adjustments. Certified accounting revenue is outside the scope of the analysis. Negative cancellation entries do not establish physical returns, and after-cancellation value is provisional. Missing customer IDs limit customer coverage, repeat purchasing reflects the observed period, and December 2011 is incomplete. The purpose of the two matching invoice pairs remains unconfirmed. [Analytical limitations](LIMITATIONS.md)

The QA summary documents independent Python reconciliations and static checks of saved Power BI visuals, alongside owner-reported interactive checks. Independent verification of the live Power BI model and its loaded mappings remains incomplete. [Quality assurance summary](QUALITY_ASSURANCE_SUMMARY.md)

## Reproduce the processed-data checks

The included [Python verifier](scripts/verify_fact_kpis.py) uses Python 3.10+ and the standard library. Run it from this directory with your own copy of the processed transaction CSV.

```sh
python scripts/verify_fact_kpis.py --fact /path/to/P001_fact_transactions.csv
```

The read-only verifier prints aggregate results and returns a nonzero exit status if a mandatory benchmark fails. Its scope is processed-fact KPI verification. Raw-workbook reconstruction, live Power BI validation and report rendering are outside that scope. The portfolio case study PDF is included. Raw and processed transaction files, the Power BI file and client-handoff reports are outside this package. [Reproducibility scope](METHODOLOGY.md) · [Recorded verification run](QUALITY_ASSURANCE_SUMMARY.md)

## Data source and attribution

Chen, D. (2015). *Online Retail*. UCI Machine Learning Repository. The dataset is licensed under CC BY 4.0. Transaction classifications, derived measures, sensitivity analyses and fictional presentation are project adaptations. No endorsement is implied. [UCI dataset](https://archive.ics.uci.edu/dataset/352/online%2Bretail) · [DOI 10.24432/C5BW33](https://doi.org/10.24432/C5BW33) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

Any license for original project code or writing remains a project-owner decision. [Data source notes](DATA_SOURCE.md) · [License and attribution notes](LICENSE_OR_ATTRIBUTION.md)
