import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)
#    calories  duration
# 0       420        50
# 1       380        40
# 2       390        45

#refer to the row index:
print(df.loc[2])
# calories    390
# duration     45
# Name: 2, dtype: int64

#use a list of indexes:
print(df.loc[[0, 2]])
#    calories  duration
# 0       420        50
# 2       390        45

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df) 
#       calories  duration
# day1       420        50
# day2       380        40
# day3       390        45

print(df.loc["day2"])
# calories    380
# duration     40
# Name: day2, dtype: int64

df = pd.read_csv('data//iris-flower-data.csv')

print(df.to_string()) 

print(pd.options.display.max_rows)
#60

#we can set max row count
pd.options.display.max_rows = 9999