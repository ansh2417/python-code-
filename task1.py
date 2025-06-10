import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

ordered_days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
average = df.groupby('day')['total_bill'].mean().reindex(ordered_days).dropna()
avg_tip = df.groupby(['day', 'smoker'])['tip'].mean().unstack().reindex(ordered_days).dropna()
x = np.arange(len(avg_tip))
w = 0.4

plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
plt.plot(average.index, average.values, marker='o', color='blue')
plt.xlabel("Day of Week")
plt.ylabel("Average Total Bill")
plt.title("Average Total Bill per Day")
plt.grid(True)

plt.subplot(2, 2, 2)
sns.boxplot(x='day', y='total_bill', data=df, order=ordered_days)
plt.title("Total Bill Distribution by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")

plt.subplot(2, 2, 3)
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")

plt.subplot(2, 2, 4)
plt.bar(x - w/2, avg_tip['Yes'], width=w, label='Smoker')
plt.bar(x + w/2, avg_tip['No'], width=w, label='Non-Smoker')
plt.xticks(x, avg_tip.index)
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.title("Average Tip by D ay (Smoker vs Non-Smoker)")
plt.legend(loc=0)

plt.tight_layout()
plt.show()
