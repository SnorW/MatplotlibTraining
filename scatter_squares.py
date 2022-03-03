import matplotlib.pyplot as plt

x_label = range(1, 1001)
y_label = [x**2 for x in x_label]

print(x_label)
print(y_label)

fig, axs = plt.subplots()
axs.plot(x_label, y_label, linewidth=2, c='r')
axs.scatter(x_label, y_label, c=y_label, cmap=plt.cm.Blues, s=10)

axs.axis = ([0, 1100, 0, 11000000])

plt.show()
