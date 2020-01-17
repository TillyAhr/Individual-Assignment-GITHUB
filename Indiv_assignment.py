import json

# Opening json file with only Indonesia in 2004
with open('conflict_indo_2004.json', encoding='utf8') as file:
    conflict_data_indo = json.load(file)

# Creating csv file with only Indonesia in 2004 and selecting only few entries
with open('conflict_data_indo.csv', 'w', encoding='utf8') as file:
    file.write('id, year, conflict_name, country, date_start, best \n')
    for violence in conflict_data_indo:
        file.write(f'{violence["id"]}, {violence["year"]}, {violence["conflict_name"]}, {violence["country"]}, {violence["date_start"]}, {violence["best"]} \n')



# Opening json file with all year for Indonesia
with open('conflict_indonesia.json', encoding='utf8') as file:
    conflict_indonesia = json.load(file)

# Creating csv file with all year for Indonesia and selecting only few entries
with open('conflict_indonesia.csv', 'w', encoding='utf8') as file:
    file.write('id, year, conflict_name, country, date_start, best, type_of_violence \n')
    for violence in conflict_indonesia:
        file.write(f'{violence["id"]}, {violence["year"]}, {violence["conflict_name"]}, {violence["country"]}, {violence["date_start"]}, {violence["best"]}, {violence["type_of_violence"]} \n')