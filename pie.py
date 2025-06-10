import matplotlib.pyplot as plt

x = [10,20,30]
y = [40,50,60]
labl = ["apple","banana","cherry"]

plt.pie(x,labels=labl)
plt.bar(x,y)

plt.show()