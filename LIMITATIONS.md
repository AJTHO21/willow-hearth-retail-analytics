# Limitations and eight unresolved exceptions

Willow & Hearth Retail and Sarah Mitchell are fictional. This self-directed simulated client engagement used public historical data. No real client approval or paid engagement occurred. The simulated client engagement was internally approved and closed on November 17, 2026, under documented analytical limitations and with eight unresolved exceptions. The internal sign-off covered the simulated client handoff only. This public portfolio presents selected work from the self-directed project.

The extract covers 1 December 2010–9 December 2011; December 2011 covers only days 1–9 and the last day is partial. Candidate merchandise sales are positive qualifying transaction value before cancellation adjustments, not certified revenue. Cancellations are negative entries, not verified customer returns. After-cancellation value is provisional, not accounting-certified net revenue. Observed repeat purchasing is purchasing frequency within the selected window, not formal retention or customer lifetime value. Missing CustomerIDs limit population coverage. Profit, margins, marketing ROI, inventory availability, fulfilment and recurring seasonality cannot be established.

### 1. Suspected full reversals

Evidence: 2 transaction pairs; GBP 245,653.20. Accepted as a disclosed uncertainty on November 15, 2026; **not factually resolved**. Preserve both legs in official reporting; exclude only four rows of the documented two pairs in separately labelled sensitivities. Purpose remains unconfirmed: not verified refunds, returns, errors or corrections.

### 2. Unmatched large cancellations

Evidence: 2 unmatched in top 10 reviewed lines. Accepted as a disclosed uncertainty on November 15, 2026; **not factually resolved**. Retain negative values. Two unmatched lines are among the ten reviewed largest lines, not all unmatched records. Matching entries may be outside the extract.

### 3. Duplicate candidates

Evidence: 5,268 extra matches; GBP 21,740.98 signed value. Accepted as a disclosed uncertainty on November 15, 2026; **not factually resolved**. Preserve duplicate candidates pending source verification; no silent deduplication or claim that all matches are errors.

### 4. Missing customer identification

Evidence: GBP 1,510,366.41 unattributed candidate merchandise value. Accepted as a disclosed uncertainty on November 15, 2026; **not factually resolved**. Keep unidentified sales in financial totals; exclude blank, empty and whitespace-only IDs from identified-customer counts; never pool unidentified sales into one customer.

### 5. Product description conflicts

Evidence: 650 product codes. Accepted as a disclosed uncertainty on November 15, 2026; **not factually resolved**. Use provisional descriptions; preserve case-distinct SKU identity with ProductModelKey rather than merging labels or raw normalized keys.

### 6. Item classification review

Evidence: 1014 flagged rows. Accepted as a disclosed uncertainty on November 15, 2026; **not factually resolved**. Preserve unreviewed merchandise classifications and flags; do not imply every classification is business-confirmed.

### 7. Partial reporting period

Evidence: 2011-12. Accepted as a disclosed uncertainty on November 15, 2026; **not factually resolved**. Label December 2011 incomplete; no full-month deterioration claim, recurring seasonality claim or unqualified extrapolation.

### 8. Bad-debt accounting adjustments

Evidence: 3 rows; GBP -11,062.06 signed. Accepted as a disclosed uncertainty on November 15, 2026; **not factually resolved**. Keep bad-debt entries in the source but outside merchandise measures; accounting treatment remains unconfirmed.

## Verification

Earlier independent Python source/fact QA reconciled the principal benchmarks and exact four-row sensitivity. Saved PBIX JSON independently establishes label v2 on both product charts, the detail table and all TopN label references. Prior four-page visual/slicer testing and full-period/November live comparisons are owner-reported manual evidence. The owner now reports manual approval of the current 7-page report, 5-page appendix and 4-page dashboard. Assignment 013 performs static file/content checks, not a new rendered visual inspection or live-engine execution.

No .bim/.tmdl/DataModelSchema export is available. Compressed model relationships, deployed expressions and every loaded product mapping were not independently extracted. Active many-to-one ProductModelKey/CustomerID/DateKey relationships with single-direction dimension-to-fact filtering are attributed manual evidence. ProductModelKey, not raw ProductKey, is the current product relationship. Historical model guidance is not current implementation guidance.

The current PBIX hash differs from Assignment 010; the three retained product visual definitions were unchanged in Assignment 011B, but no prior DataModel fingerprint exists. Cosmetic-only classification and model equivalence remain unverified. The new document approval does not explicitly bind the earlier live tests to the current PBIX hash. Before any external distribution of the PBIX, record owner confirmation of current-version test coverage/change scope, or perform only the relevant targeted current-model checks. Do not repeat completed source QA merely because the hash changed.
