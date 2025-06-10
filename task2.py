import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
avg_bill = df.groupby('day')['total_bill'].mean().reindex(days).dropna()
avg_tip = df.groupby(['day', 'smoker'])['tip'].mean().unstack().reindex(days).dropna()
x = np.arange(len(avg_tip))
w = 0.4

plt.figure(figsize=(12, 10))

plt.subplot(4 ,4, 1)
plt.plot(avg_bill.index, avg_bill.values, marker='o')
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.title("Average Total Bill per Day")

plt.subplot(4, 4, 2)
sns.boxplot(x='day', y='total_bill', data=df, order=days)
plt.title("Total Bill by Day")

plt.subplot(4, 4, 3)
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")

plt.subplot(4, 4, 4)
plt.bar(x - w/2, avg_tip['Yes'], width=w, label='Smoker')
plt.bar(x + w/2, avg_tip['No'], width=w, label='Non-Smoker')
plt.xticks(x, avg_tip.index)
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.title("Average Tip by Day (Smoker vs Non-Smoker)")
plt.legend()


plt.subplot(4, 4, 5)
plt.plot(avg_bill.index, avg_bill.values, marker='o')
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.title("Average Total Bill per Day")

plt.subplot(4, 4, 6)
sns.boxplot(x='day', y='total_bill', data=df, order=days)
plt.title("Total Bill by Day")

plt.subplot(4, 4, 7)
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")

plt.subplot(4, 4, 8)
plt.bar(x - w/2, avg_tip['Yes'], width=w, label='Smoker')
plt.bar(x + w/2, avg_tip['No'], width=w, label='Non-Smoker')
plt.xticks(x, avg_tip.index)
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.title("Average Tip by Day (Smoker vs Non-Smoker)")
plt.legend()


plt.subplot(4, 4, 9)
plt.plot(avg_bill.index, avg_bill.values, marker='o')
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.title("Average Total Bill per Day")

plt.subplot(4, 4, 10)
sns.boxplot(x='day', y='total_bill', data=df, order=days)
plt.title("Total Bill by Day")

plt.subplot(4, 4, 11)
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")

plt.subplot(4, 4, 12)
plt.bar(x - w/2, avg_tip['Yes'], width=w, label='Smoker')
plt.bar(x + w/2, avg_tip['No'], width=w, label='Non-Smoker')
plt.xticks(x, avg_tip.index)
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.title("Average Tip by Day (Smoker vs Non-Smoker)")
plt.legend()


plt.subplot(4, 4, 13)
plt.plot(avg_bill.index, avg_bill.values, marker='o')
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.title("Average Total Bill per Day")

plt.subplot(4, 4, 14)
sns.boxplot(x='day', y='total_bill', data=df, order=days)
plt.title("Total Bill by Day")

plt.subplot(4, 4, 15)
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")

plt.subplot(4, 4, 16)
plt.bar(x - w/2, avg_tip['Yes'], width=w, label='Smoker')
plt.bar(x + w/2, avg_tip['No'], width=w, label='Non-Smoker')
plt.xticks(x, avg_tip.index)
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.title("Average Tip by Day (Smoker vs Non-Smoker)")
plt.legend()

plt.tight_layout()
plt.show()
