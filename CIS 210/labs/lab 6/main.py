data_list = []
with open('november_rain.csv', 'r') as f:
    # TODO: read lines from file and process them!
    for line in f:
        data_list.append(line.split(','))

data_dict = {}
for [yearmo, value] in data_list:
    year = int(yearmo[:4])
    data_dict[year] = float(value)
print(data_dict)

data_dict = {int(yearmo[:4]): float(value) for [yearmo, value] in data_list}

rainfall_values = list(data_dict.values())

# pt. 2

mean_rainfall = sum(rainfall_values) / len(rainfall_values)

import matplotlib.pyplot as plt

plt.plot(data_dict.keys(), rainfall_values)
plt.axhline(y=mean_rainfall, linestyle='dotted', color='red')
plt.show()
# pt.3
high_rain_years = [year for year, rainfall in data_dict.items() if rainfall >= 1.5 * mean_rainfall]

with open('out.txt', 'w') as f:
    [f.write(f'year:{year}, rainfall: {data_dict[year]}\n') for year in high_rain_years]
