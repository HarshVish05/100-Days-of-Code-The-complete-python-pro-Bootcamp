import pandas
# output - fur color count
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240527.csv')
# print(data['Primary Fur Color'].value_counts().to_list())

# unique function returns a numpy array so i have used tolist to convert it into a list
# dropna drops all the NaN values.
data_dict = {
    "Fur Color" : data['Primary Fur Color'].dropna().unique().tolist(),
    "count" : data['Primary Fur Color'].value_counts().to_list()
} 

dataframe = pandas.DataFrame(data= data_dict)
# print(dataframe)
dataframe.to_csv("squirrel_count.csv")