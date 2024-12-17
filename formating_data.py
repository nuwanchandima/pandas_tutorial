import pandas as pd

df = pd.read_csv('data//formating_data.csv')
#this remove row with empty cell
df.dropna(inplace = True)
#print(df.to_string())

#Replace Empty Values
df1 = pd.read_csv('data//formating_data.csv')
df1.fillna(130, inplace = True)
#print(df1.to_string())

#Replace Only For Specified Columns
df2 = pd.read_csv('data//formating_data.csv')
df2["Calories"].fillna(130, inplace = True)
df2["Date"].fillna("'2024/11/21'", inplace = True)
#print(df2.to_string())

#Replace Using Mean, Median, or Mode
df3 = pd.read_csv('data//formating_data.csv')
mean = df3["Calories"].mean() #the average value 
median = df3["Calories"].median() #the value in the middle
mode = df3["Calories"].mode()[0] #the value that appears most frequently
df3["Calories"].fillna(mean, inplace = True)
df3["Date"].fillna("'2024/11/21'", inplace = True)
#print(mean,median,mode)
#print(df3.to_string())