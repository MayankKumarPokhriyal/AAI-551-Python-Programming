import matplotlib.pyplot as plt

# initializing the data
x = [1, 2, 3, 4, 5]
y = [-50, 50, -50, 50, -50]

# plotting the data
plt.plot(x, y)

# Adding the title
plt.title("Simple Graph")

# Adding the labels
plt.xlabel("Minutes")
plt.ylabel("Value")

plt.show()