import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

states = ['Maharashtra', 'Gujarat', 'Karnataka', 'Tamil Nadu', 'Rajasthan', 'Uttar Pradesh', 'Bihar', 'West Bengal']
branches = ['AEIB-MH', 'AEIB-GJ', 'AEIB-KA', 'AEIB-TN', 'AEIB-RJ', 'AEIB-UP', 'AEIB-BR', 'AEIB-WB']
manager_names = ['Rajesh Sharma', 'Priya Mehta', 'Amit Verma', 'Sneha Gupta', 'Vikram Joshi', 'Anjali Rao', 'Manoj Patel', 'Neha Singh']

np.random.seed(0)
accounts = []
account_number = 10001

for i in range(8):
    for j in range(np.random.randint(30, 50)):
        balance = np.random.randint(5000, 200000)
        has_loan = np.random.choice([True, False], p=[0.6, 0.4])
        loan_amount = np.random.randint(50000, 500000) if has_loan else 0
        interest = loan_amount * 0.08 if has_loan else 0
        emi_status = np.random.choice(['Paying', 'Not Paying']) if has_loan else 'N/A'
        accounts.append({
            'Account Number': account_number,
            'Customer Name': f'Customer_{account_number}',
            'State': states[i],
            'Branch Code': branches[i],
            'Branch Manager': manager_names[i],
            'Balance': balance,
            'Has Loan': has_loan,
            'Loan Amount': loan_amount,
            'Interest': interest,
            'EMI Status': emi_status
        })
        account_number += 1

df = pd.DataFrame(accounts)
df.to_csv('aeib.csv', index=False)

print("\n----- AEIB BANK MANAGEMENT SUMMARY -----")
print("Total Accounts in Bank:", len(df))
print("Total Balance in All Accounts: ₹", df['Balance'].sum())
print("Total Loan Amount Given: ₹", df['Loan Amount'].sum())
print("Total Interest to be Received: ₹", df['Interest'].sum())

loan_customers = df[df['Has Loan'] == True]
print("Customers Paying EMI:", loan_customers[loan_customers['EMI Status'] == 'Paying '].shape[0])
print("Customers Not Paying EMI:", loan_customers[loan_customers['EMI Status'] == 'Not Paying'].shape[0])

print("\nAccounts per State:")
print(df['State'].value_counts())

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

loan_pivot = df.pivot_table(
    values='Loan Amount', index='State', columns='EMI Status', aggfunc='sum', fill_value=0
)
sns.heatmap(loan_pivot, annot=True, fmt=".0f", cmap='YlGnBu', ax=ax1)
ax1.set_title('Loan Amount by State and EMI Status')

sns.boxplot(x='State', y='Balance', data=df, ax=ax2)
ax2.set_title('Account Balance Distribution by State')
ax2.tick_params(axis='x', rotation=45)

for ax in [ax1, ax2]:
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False, bottom=False)
    ax.grid(False)

plt.tight_layout()
plt.show()
