import json

with open('Individual_Assignment_GIT/conflict_indo_2004.json', encoding='utf8') as file:
    conflict_data_indo = json.load(file)


with open('Individual_Assignment_GIT/conflict_data_indo.csv', 'w', encoding='utf8') as file:
    file.write('id, year, conflict_name, country, date_start, best \n')
    for violence in conflict_data_indo:
        file.write(f'{violence["id"]}, {violence["year"]}, {violence["conflict_name"]}, {violence["country"]}, {violence["date_start"]}, {violence["best"]} \n')