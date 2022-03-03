import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as file:
    reader = csv.reader(file)
    headers_row = next(reader)

    highs = []
    lows = []
    dates = []

    for row in reader:
        try:
            high = int(row[4])
            low = int(row[5])
            date = datetime.strptime(row[2], '%Y-%m-%d').date()
        except ValueError:
            print(f'Data missing of day: {date}')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)


plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='r', alpha=0.5)
ax.plot(dates, lows, c='b', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='b', alpha=0.1)


# format
ax.set_title('Death valley daily temperature of 2018', fontsize=24)
plt.xlabel('Dates', fontsize=14)
plt.ylabel('Temeperature(F°)', fontsize=14)

fig.autofmt_xdate()

plt.show()