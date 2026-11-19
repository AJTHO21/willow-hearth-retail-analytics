# Data source and handling

Chen, D. (2015), *Online Retail*, UCI Machine Learning Repository. [Dataset](https://archive.ics.uci.edu/dataset/352/online%2Bretail), [DOI 10.24432/C5BW33](https://doi.org/10.24432/C5BW33), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Classifications, derived measures, sensitivities and fictional presentation are project adaptations; no endorsement is implied.

The project used the original Online Retail.xlsx with 541,909 rows, observed from 2010-12-01 08:26 to 2011-12-09 12:50. Obtain the workbook from the official source independently; this repository does not bundle it. Catalogue summary metadata does not override verified missing CustomerIDs in the local extract. No fictional client supplied these records.

The included verifier requires the project-format processed fact CSV, with InvoiceNo, CustomerID, ProductKey, Quantity, LineValue, InvoiceDate, TransactionType and ItemType columns. It preserves source identifiers and uses explicit customer eligibility. No personal/customer transaction records are distributed; verifier output is aggregate only. Obtaining the raw workbook alone does not automatically produce that classified fact export; reconstruction of the classification pipeline is outside this reduced publication package.
