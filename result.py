import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('result.csv')

df['Credit Points'] = df['Credit'] * df['Grade Point']

total_credits = df['Credit'].sum()
total_credit_points = df['Credit Points'].sum()

sgpa = total_credit_points / total_credits
percentage = (sgpa - 0.75) * 10 

print("Total Credits:", total_credits)
print("Total Credit Points:", total_credit_points)
print("SGPA:", round(sgpa, 2))
print("Approx. Percentage:", round(percentage, 2), "%")

plt.figure(figsize=(10, 6))
plt.bar(df['Course Title'], df['Grade Point'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title("Grade Points per Subject")
plt.ylabel("Grade Point")
plt.xlabel("Subjects")
#plt.tight_layout()
#plt.grid(True)
plt.show()
