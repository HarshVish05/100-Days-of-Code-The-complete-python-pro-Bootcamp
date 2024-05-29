# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)    # returns a csv data object
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas
# refer to panda docs for more methods

data = pandas.read_csv("weather_data.csv")
# print(data)

# getting data of a coloumn
# print(len(data['temp']))
# print(data.temp)

# Getting data of each row of a dataframe
# print(data[data['day'] == 'Monday'])
monday = data[data.day == 'Monday']
# print(len(monday))
# print(monday.condition)
# print(monday.temp[0])


# create a dataframe from scratch
data_dict = {
    "students": ['Nandu', 'Chandu', 'Bandu'],
    "scores":[54, 67 ,87]
}

dataframe_data = pandas.DataFrame(data= data_dict)
dataframe_data.to_csv("new_data.csv")  # it only takes one argument which is the path 
# print(dataframe_data)

# looping through dataframes
# for key,value in dataframe_data.items():
#     print(value)

# looping through each rows of dataframes
for index, row in dataframe_data.iterrows():
    # print(index)
    # print(row.students) # each row is a panda series object
    if row.students == 'Chandu':
        print(row.scores)



# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)

# challenge - calculate the average temperature
# temp_list = data['temp'].to_list()

# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)

# another way
# print(data['temp'].mean())

# challenge - find max value in temp list using series 
# max_temp = data['temp'].max()
# print(max_temp)

# challenge - Print the row which has maximum temperature
# print(data[data.temp == data.temp.max()])