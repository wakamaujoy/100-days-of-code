#                  analysing data using files in python
# with open('weather_data.csv') as weather:
#     data = weather.readlines()
#     print(data)

#                   analysis of data using inbuilt csv
# import csv
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temp = []
#     # print(data)
#     for item in data:
#         if item[1] != "temp":
#             item_int = int(item[1])
#             temp.append(item_int)
#     # print(temp)

#                    analysis of data using pandas library

import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# print(data.temp.max())
# print(data["temp"].max())



# convert data frame to a dictionary
# data_dict = data.to_dict()
# print(data_dict)



# convert data to a list
# data_list = data.temp.to_list()
# print(data_list)
#

# get row data of a dataframe
# print(data[data.day == "Monday"])
# get the row of data with the maximum temp===get the dataframe, narrow down to the series then set a condition
# print(data[data.temp == data.temp.max()])




# #           getting attributes in a row
# mon_raw = data[data.day == "Monday"]
# print(mon_raw.condition)

# create a dataframe from scratch
# data_dict = {
#    "names":["Jane", "Joe", "Jim"],
#     "marks":[30,33,38]
# }
# print(pandas.DataFrame(data_dict))


squirrel_data = pandas.read_csv("Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_length = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_length = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_length = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
# print(gray_squirrels)
print(gray_squirrels_length)
print(cinnamon_squirrels_length)
print(black_squirrels_length)


squirrel_data_dict = {
    "squirrel_color": ["gray", "cinnamon", "black"],
    "squirrels_number": [gray_squirrels_length,cinnamon_squirrels_length,black_squirrels_length]
}
# TO A DATAFRAME
squirrel_data_dataframe = pandas.DataFrame(squirrel_data_dict)
print(squirrel_data_dataframe)

# TO CONVERT THE DATAFRAME TO CSV
squirrel_data_dataframe.to_csv("Squirrel_Count_based_on_color")