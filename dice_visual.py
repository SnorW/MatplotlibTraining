from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


die_1 = Die()
die_2 = Die(10)

results = []

for num_rolls in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# GRAPH

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies, width=2)]

x_axis_config = {'title': "2 Dice's sid es"}
y_axis_config = {'title': "Frequencies of dice's sides"}

my_layout = Layout(title='Results of rolling one D6 and one D10 50_000 times', xaxis=x_axis_config
                   , yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
