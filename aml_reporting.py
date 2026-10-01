import pandas as pd

data = {
    "branch": ["SP01", "SP01", "RJ02", "RJ02", "SP01", "RJ02", "SP01", "RJ02"],
    "transaction_type": ["deposit", "withdrawal", "deposit", "transfer", "transfer", "deposit", "withdrawal", "transfer"],
    "amount": [15000, 8000, 25000, 60000, 12000, 9500, 30000, 45000],
    "currency": ["BRL", "BRL", "BRL", "USD", "BRL", "BRL", "USD", "USD"],
    "aml_flag": [False, False, True, True, False, False, True, True]
}
df = pd.DataFrame(data)

# Branch x transaction type summary
pivot_report = pd.pivot_table(
    df, index='branch', columns='transaction_type',
    values='amount', aggfunc='sum', fill_value=0
)

# AML reportable transactions
reporting_threshold = 10000
df['requires_reporting'] = df['amount'] > reporting_threshold
reportable_df = df[df['requires_reporting']]

print(pivot_report)
print(reportable_df)

pivot_report.to_csv("branch_transaction_report.csv")
reportable_df.to_csv("aml_reportable_transactions.csv", index=False)