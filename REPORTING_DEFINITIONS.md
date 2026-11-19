# Reporting definitions

- Candidate merchandise sales: sum LineValue for TransactionType="Candidate sale" AND ItemType="Merchandise / unreviewed".
- Merchandise cancellations: signed sum LineValue for TransactionType="Cancellation" with the same item filter.
- After-cancellation merchandise value: sum of the preceding values; provisional, not certified net revenue.
- Merchandise orders: distinct InvoiceNo among qualifying sales; AOV = candidate value / orders.
- Identified customers: distinct nonblank CustomerID among qualifying sales; null/empty/whitespace IDs excluded from counts, financial value retained.
- Observed repeat purchasers: eligible IDs with two or more distinct qualifying invoices in the selected window; rate divides by eligible purchasing customers in that same window. Not retention.
- Products sold / positive units: distinct exact case-sensitive source product identities / sum qualifying sale Quantity. ProductModelKey preserves that identity in the deployed relationship; source CSV ProductKey remains provenance, not a safe case-insensitive relationship key.
- Product Display Label v2: saved chart categories, detail table and TopN label bindings. Description is provisional; no deployment formula is invented.
- Two-pair sensitivity: exclude only complete invoices 541431, C541433, 581483, C581484 (four rows), both legs, only in a separate analytical view. Official measures remain unchanged.
- Dates: cancellation date determines cancellation month. Repeat/customer/product counts are recalculated for the selected window, not summed across months. December 2011 is partial.

The extract covers 1 December 2010–9 December 2011; December 2011 covers only days 1–9 and the last day is partial. Candidate merchandise sales are positive qualifying transaction value before cancellation adjustments, not certified revenue. Cancellations are negative entries, not verified customer returns. After-cancellation value is provisional, not accounting-certified net revenue. Observed repeat purchasing is purchasing frequency within the selected window, not formal retention or customer lifetime value. Missing CustomerIDs limit population coverage. Profit, margins, marketing ROI, inventory availability, fulfilment and recurring seasonality cannot be established.
