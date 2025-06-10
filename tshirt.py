import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("tshirt.csv")

data["Year"] = [f"Year {i}" for i in range(1, len(data) + 1)]

total_revenue = data["Total_Revenue"].sum()
total_cost = data["Total_Cost"].sum()
total_profit = data["Profit"].sum()
average_profit = data["Profit"].mean()

print("Total Revenue (10 years):", total_revenue)
print("Total Cost (10 years):", total_cost)
print("Total Profit (10 years):", total_profit)
print("Average Profit per Year:", average_profit)

plt.bar(data["Year"], data["Profit"], color='orange')
plt.title("Yearly Profit from T-Shirt Business")
plt.xlabel("Year")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()
