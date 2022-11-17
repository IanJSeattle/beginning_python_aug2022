from pprint import pprint as pp

temps = {}
temps['seattle'] = [
                     [1200, 20],
                     [1300, 21],
                     [1400, 23]
                   ]
temps['orlando'] = [[1200, 29], [1300, 31], [1400, 32]]
temps['san diego'] = [[1200, 27], [1300, 30], [1400, 31]]

for city, temp_list in temps.items():
    print(f'The time vs. temp chart in {city} was:')
    for time_temp in temp_list:
        print(f'\tTime: {time_temp[0]} Temp: {time_temp[1]}')
