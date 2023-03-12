# with open("weather_data.csv") as data_files:
#     data = data_files.readlines()
#     print(data)
#
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
data_dict = data.to_dict()
print(data_dict)

data_list = data["temp"].to_list()
print(data_list)


def average(list):
    return sum(list) / len(list)

average_num = average(data_list)

round_num = round(average_num, 2)
print(round_num)

print(data["temp"].mean())


