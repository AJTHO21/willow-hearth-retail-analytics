# Willow & Hearth Retail — from transaction records to a qualified business story

## 1. Project overview

Willow & Hearth Retail and Sarah Mitchell are fictional. This self-directed simulated client engagement used public historical data. No real client approval or paid engagement occurred. The simulated client engagement was internally approved and closed on November 17, 2026, under documented analytical limitations and with eight unresolved exceptions. The internal sign-off covered the simulated client handoff only. This public portfolio presents selected work from the self-directed project. The work converts 541,909 historical transaction rows into a documented analytical model, a four-page Power BI dashboard and management-facing findings. This demonstrates analytical process and communication, not implemented commercial results.

## 2. Simulated business problem

A fictional small retailer needs to understand merchandise value, order activity, identifiable customer purchasing, products and geographic concentration without confusing cancellation entries with physical returns or candidate sales with certified revenue.

## 3. Public dataset and attribution

Chen, D. (2015), *Online Retail*, UCI Machine Learning Repository. [Dataset](https://archive.ics.uci.edu/dataset/352/online%2Bretail), [DOI 10.24432/C5BW33](https://doi.org/10.24432/C5BW33), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Classifications, derived measures, sensitivities and fictional presentation are project adaptations; no endorsement is implied. The fictional identities are an adaptation, not the source business's identity. No private client dataset was used.

## 4. Analytical objectives

Compare complete observed months; distinguish invoice volume from average value; measure identified purchasing frequency; compare sales and unit rankings; expose account concentration and material transaction exceptions; make every headline claim traceable.

## 5. Tools and technology

Python CSV/Decimal and the project's pandas/NumPy/openpyxl processing environment; CSV analytical exports; Power BI Desktop and DAX; Markdown documentation; Word and PDF report formats; SHA-256 manifests. Production constraints and manually completed report review are disclosed rather than presented as automated rendering success.

## 6. Data cleaning and transformation

All 541,909 original records were retained, with original row references, invoices and source product/customer identities. Transaction and item classifications separate candidate sales, cancellations and non-merchandise exceptions. Duplicate candidates are flagged, not automatically removed. Fact and dimension tables support analysis. Missing customer identifiers remain in financial totals; blank/empty/whitespace IDs are excluded from identified-customer metrics. ProductModelKey preserves exact case-sensitive SKU identity rather than normalizing colliding raw ProductKeys.

## 7. Reporting definitions and QA

Candidate sales use TransactionType = Candidate sale and ItemType = Merchandise / unreviewed. Cancellations use Cancellation with the same item filter and retain negative signs. Independent reconciliations check financial, customer, product and monthly measures, keys, records and sensitivity boundaries. Mandatory checks fail with nonzero status. Source hashes distinguish historical evidence from current files. The publication verifier reproduces processed-fact KPIs without distributing transaction data; it is not a raw-workbook rebuild.

## 8. Power BI dashboard

Executive Overview, Sales Performance, Customer Analytics and Product Performance present financial, order, purchasing-frequency and product views. The saved product charts, detail table and TopN bindings use Product Display Label v2. Owner-assisted interactive tests and current document approvals are attributed evidence; independent archive/source checks are a separate class. No unverified screenshots are embedded in this case study.

## 9. Five principal findings

1. **November growth and identification coverage:** October-to-November candidate sales rose 31.72%, orders 37.21%, while average order value fell 4.00%. Unidentified transactions account for 21.65% of November sales and 61.12% of the October-to-November increase: different denominators, not evidence of a marketing or checkout cause.
2. **Matching invoice pairs affect rankings:** GBP 245,653.20 of positive value has equal negative legs, representing 51.31% of cancellation magnitude. A separately labelled sensitivity excludes only 541431/C541433 and 581483/C581484 (four rows). Candidate sales move from GBP 10,271,433.06 to GBP 10,025,779.86; cancellations from GBP -478,724.18 to GBP -233,070.98. After-cancellation value remains GBP 9,792,708.88. SKU 23843 has GBP 0.00 remaining qualifying sales within that sensitivity; no out-of-period demand conclusion follows.
3. **Geographic concentration is account concentration:** the UK contributes 85.16% of candidate sales. The largest identified accounts represent 98.33% of Netherlands and 90.15% of Australian candidate sales. These totals do not demonstrate broad international demand.
4. **Observed repeat purchasing matters:** 2,829 of 4,334 identified purchasers had at least two qualifying invoices, giving 65.27%. They contribute 92.82% of identified candidate sales. This is not formal retention, loyalty effectiveness or lifetime value; unidentified sales are GBP 1,510,366.41 (14.70% of candidate value).
5. **Product value and volume answer different questions:** the Top 5 by candidate sales represent 6.24% of total candidate sales across 3,908 sold SKUs. Official sales ranking begins 22423, 23843, 85123A, 47566, 85099B. Unit ranking begins 23843, 23166, 22197, 84077, 85099B. In the two-pair sensitivity, 22423 remains the value leader and 22197 leads units. Neither ranking establishes profit or stock requirements.

Full-period orders total 19,773; positive merchandise units total 5,577,103. Official financial and customer measures are preserved, not replaced with sensitivity results.

## 10. Proportionate recommendations

Investigate customer-identifier capture; obtain original links/reason codes for matching invoices; review November order sources and operational records; understand concentrated overseas accounts; obtain costs, stock, pack-size and fulfilment data before product decisions. No unsupported spending, pricing, inventory or expansion recommendation is made.

## 11. Challenges and solutions

Case-insensitive raw SKU collisions required model-safe identity rather than destructive normalization. Empty identifiers required explicit customer eligibility rather than forcing benchmark agreement. Large matching positive/negative entries required parallel official/sensitivity views, not deletion. Partial December and changing saved-file hashes required explicit period/version controls. Toolchain limitations were recorded; owner visual review is not misrepresented as independent automation.

## 12. Limitations and unresolved questions

The extract covers 1 December 2010–9 December 2011; December 2011 covers only days 1–9 and the last day is partial. Candidate merchandise sales are positive qualifying transaction value before cancellation adjustments, not certified revenue. Cancellations are negative entries, not verified customer returns. After-cancellation value is provisional, not accounting-certified net revenue. Observed repeat purchasing is purchasing frequency within the selected window, not formal retention or customer lifetime value. Missing CustomerIDs limit population coverage. Profit, margins, marketing ROI, inventory availability, fulfilment and recurring seasonality cannot be established.

All eight exceptions remain disclosed and unresolved: suspected full reversals, unmatched large cancellations, duplicate candidates, missing customer identification, product description conflicts, item classification review, partial reporting period and bad-debt accounting adjustments. Their reporting restrictions are recorded separately. Document approval and accepted uncertainty do not factually close them.

Earlier independent Python source/fact QA reconciled the principal benchmarks and exact four-row sensitivity. Saved PBIX JSON independently establishes label v2 on both product charts, the detail table and all TopN label references. Prior four-page visual/slicer testing and full-period/November live comparisons are owner-reported manual evidence. The owner now reports manual approval of the current 7-page report, 5-page appendix and 4-page dashboard. Assignment 013 performs static file/content checks, not a new rendered visual inspection or live-engine execution.

No .bim/.tmdl/DataModelSchema export is available. Compressed model relationships, deployed expressions and every loaded product mapping were not independently extracted. Active many-to-one ProductModelKey/CustomerID/DateKey relationships with single-direction dimension-to-fact filtering are attributed manual evidence. ProductModelKey, not raw ProductKey, is the current product relationship. Historical model guidance is not current implementation guidance.

The current PBIX hash differs from Assignment 010; the three retained product visual definitions were unchanged in Assignment 011B, but no prior DataModel fingerprint exists. Cosmetic-only classification and model equivalence remain unverified. The new document approval does not explicitly bind the earlier live tests to the current PBIX hash. Before any external distribution of the PBIX, record owner confirmation of current-version test coverage/change scope, or perform only the relevant targeted current-model checks. Do not repeat completed source QA merely because the hash changed.

## 13. Deliverables

A four-page dashboard PBIX/PDF, owner-approved 7-page findings PDF with Word companion, owner-approved 5-page technical appendix PDF with Word companion, data/model QA history, a separate clean local handoff, and publication-ready explanatory documents with a portable KPI verifier. This public package includes the [final portfolio case study PDF](assets/P001_Portfolio_Case_Study_FINAL.pdf), supporting documentation and the verifier. The simulated client-handoff deliverables and internal QA records remain separate.

## 14. Skills demonstrated

Transaction classification; data modelling; financial/customer/product reconciliation; exception investigation; DAX and Power BI report design; reproducibility and preservation controls; qualified business interpretation; plain-language reporting and evidence-based handoff.
