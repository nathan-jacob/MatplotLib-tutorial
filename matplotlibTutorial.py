import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,6,7]

x2 = [1,2,3]
y2 = [10,14,12]


plt.plot(x,y, label="First Line")
plt.plot(x2,y2, Label = "Second Line")

#add labels
plt.xlabel("Plot Number")
plt.ylabel("Important Var")


plt.title("Interesting Graph")
plt.legend()
plt.show()
