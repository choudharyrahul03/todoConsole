import csv

city_name = input("Enter city name: ")
with open("cities.csv","r") as file:
    content = list(csv.reader(file))
    for i in content[1:]:
        if i[0] == city_name:
            print(i[1])