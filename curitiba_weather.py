import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'data/curitiba_weather.csv'

with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    name = ''
    average_celcius = []
    average_fareheint = []
    dates = []
    for row in reader:
        avgF = float(row[3].replace('"', ''))
        avg = float(f'{(avgF - 32) * 5 / 9:.2f}')
        name = row[1]
        date = datetime.strptime(row[2], '%Y-%m-%d').date()
        dates.append(date)
        average_fareheint.append(avgF)
        average_celcius.append(avg)

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, average_celcius, c='g', label='Temperature C°')
ax.legend()

# format
fig.autofmt_xdate()
ax.set_title("Curitiba's average temperatures ", fontsize=24)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Temperature', fontsize=14)
ax.tick_params(axis='both', which='major')

plt.show()
