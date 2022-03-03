import matplotlib.pyplot as plt

x_cubes = range(1, 5001)
x_cubes_5 = range(1, 6)
y_cubes = [x**3 for x in x_cubes]
y_cubes_5 = [x**3 for x in x_cubes_5]

fig, axs = plt.subplots()

axs.plot(x_cubes, y_cubes, c='b', linewidth=2)
axs.plot(x_cubes_5, y_cubes_5, c='r', linewidth=3)

plt.show()





