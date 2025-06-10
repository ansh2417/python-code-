import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("car.csv")
#b= pd.to_datetime(data["Month"])
data["Month"]= pd.to_datetime(data["Month"])
#print(b)

plt.figure(figsize=(15,5))
plt.plot(data["Month"],data["Sales"], marker='o')
plt.title("Monthly car sales over time")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()