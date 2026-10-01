# AML Transaction Reporting

A Python script that summarizes branch transaction activity and flags transactions exceeding a regulatory reporting threshold — a simplified version of Anti-Money Laundering (AML) compliance reporting used in banking.

## How it works
- Builds a pivot table summarizing total transaction amounts by branch and transaction type
- Flags any transaction above a reporting threshold ($10,000) as requiring regulatory reporting
- Exports both the branch summary and the reportable transactions to CSV files

## How to run
```bash
python aml_reporting.py
```
This generates two CSV files: `branch_transaction_report.csv` and `aml_reportable_transactions.csv`.

## What I learned
- Using `pd.pivot_table()` to summarize data across two categorical dimensions (branch, transaction type)
- Using `fill_value=0` to handle combinations with no data, instead of showing `NaN`
- Applying a boolean threshold condition to flag rows (`df['amount'] > threshold`)
- Filtering a DataFrame down to only flagged rows
- Exporting results with `.to_csv()` for downstream use or reporting

## Dependencies
Requires pandas:
```bash
pip install pandas
```
