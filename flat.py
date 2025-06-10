import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("flat.csv")
data["Price"] = pd.to_numeric(data["Price"])

total_rooms = len(data)
total_earning = data["Price"].sum()
average_price = data["Price"].mean()

print("Total Rooms Sold:", total_rooms)
print("Total Earning:", total_earning)
print("Average Room Price:", average_price)

yearly_sales = data.groupby("Sold_Year")["Price"].sum().reset_index()

plt.plot(yearly_sales["Sold_Year"], yearly_sales["Price"], marker='o', color='blue')
#plt.bar(data["Sold_Year"], data["Price"], color='orange')
plt.title("Yearly Flat Room Sales")
plt.xlabel("Year")

plt.ylabel("Total Earning")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
