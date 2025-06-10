import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7]
y = [1,2,3,4,5,6,7,8]
z = [0,1,2,3,4,5,6,7]

plt.subplot(1,1,1)
plt.plot(x,y)

plt.subplot(1,2,2)
plt.plot(x,z)

plt.subplot(2,1,1)
plt.plot(x,z)

plt.subplot(2,2,2)
plt.plot(x,z)

plt.legend()
plt.savefig("graph2.png")
plt.show()