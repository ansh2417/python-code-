import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import string

np.random.seed(42)
random.seed(42)

num_houses = 100
house_numbers = [f"House_{i+1}" for i in range(num_houses)]
names = [''.join(random.choices(string.ascii_uppercase, k=5)) for _ in range(num_houses)]
payments = np.random.randint(5000, 30000, size=num_houses)
light_bills = np.random.randint(500, 5000, size=num_houses)
water_bills = np.random.randint(300, 2000, size=num_houses)
maintenance = np.random.randint(1000, 10000, size=num_houses)
extra_charges = np.random.randint(0, 3000, size=num_houses)

df = pd.DataFrame({
    'House': house_numbers,
    'Owner': names,
    'Monthly_Payment': payments,
    'Light_Bill': light_bills,
    'Water_Bill': water_bills,
    'Maintenance': maintenance,
    'Extra_Charges': extra_charges
})

df['Total_Expense'] = df[['Monthly_Payment', 'Light_Bill', 'Water_Bill', 'Maintenance', 'Extra_Charges']].sum(axis=1)

sns.set(style="whitegrid")
fig, axs = plt.subplots(3, 2, figsize=(18, 15))

sns.histplot(df['Monthly_Payment'], kde=True, ax=axs[0, 0], color='skyblue')
axs[0, 0].set_title('Distribution of Monthly Payments')

sns.boxplot(data=df[['Light_Bill', 'Water_Bill', 'Maintenance']], ax=axs[0, 1])
axs[0, 1].set_title('Boxplot of Utility Bills')

sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm", ax=axs[1, 0])
axs[1, 0].set_title('Heatmap of Numerical Correlations')

sns.scatterplot(x='Monthly_Payment', y='Total_Expense', data=df, ax=axs[1, 1], color='purple')
axs[1, 1].set_title('Monthly Payment vs Total Expense')

sns.violinplot(data=df[['Monthly_Payment']], ax=axs[2, 0], color='orange')
axs[2, 0].set_title('Violin Plot of Monthly Payments')

sns.barplot(x='House', y='Total_Expense', data=df.sort_values('Total_Expense', ascending=False).head(10), ax=axs[2, 1])
axs[2, 1].set_title('Top 10 Houses by Total Expense')
axs[2, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
