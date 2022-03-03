import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3, )

ax.set_title('Squares values', fontsize=24)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Squares of value', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)
plt.scatter(x=input_values, y=squares, s=200)

plt.savefig('mpl_squares2.png', bbox_inches='tight')
