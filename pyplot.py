import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7]
y = [1,2,3,4,5,6,7,8]
z = [0,1,2,3,4,5,6,7]

plt.figure(figsize=(8,8))
plt.plot(x , y , marker="s" , linestyle=":" , color="black" , label="highest")
plt.plot(x , z , color="blue")
plt.title("My pyplot Graph")
plt.xlabel("X-Axis Value")
plt.ylabel("Y-Axis Value")
plt.grid()

plt.legend()
plt.savefig("graph1.png")
plt.show()