import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    dates = []
    lows = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
        date = datetime.strptime(row[2], '%Y-%m-%d').date()
        dates.append(date)
        low = int(row[6])
        lows.append(low)
    print(highs)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)

ax.fill_between(dates, highs, lows,facecolor='b', alpha=0.1)

plt.title('Daily Temperature of July 2018', fontsize=24)
plt.xlabel('Days', fontsize=16)
plt.ylabel('Temperature (F°)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()

plt.show()