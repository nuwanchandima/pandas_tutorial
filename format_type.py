import pandas as pd

#Data of Wrong Format
#Convert Into a Correct Format
df = pd.read_csv('data//formating_data.csv')
print("Raw Dates:\n", df['Date'])
# Convert the Date column to datetime, inferring formats and handling errors
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Check for rows with invalid dates
invalid_dates = df[df['Date'].isna()]
if not invalid_dates.empty:
    print("\nRows with invalid dates:\n", invalid_dates)

# Handle invalid dates: Drop rows with NaT or replace with a default value
df.dropna(subset=['Date'], inplace=True)  # Drop rows with invalid dates
# Alternatively, replace invalid dates with a specific value (e.g., a default date)
# df['Date'].fillna(pd.Timestamp('2000-01-01'), inplace=True)
mode_of_calories=df["Calories"].mode()[0]
df['Calories']=df['Calories'].fillna(mode_of_calories)

# df.loc[7, "Duration"]=45
# for x in df.index:
#   if df.loc[x, "Duration"] > 60:
#     df.loc[x, "Duration"] = 60

# Removing Rows
for x in df.index:
  if df.loc[x, "Duration"] > 60:
    df.drop(x,inplace=True)

# Inspect the cleaned DataFrame
print("\nCleaned DataFrame:\n", df.to_string())

# Discovering Duplicates
print(df.duplicated())
# Removing Duplicates
df.drop_duplicates(inplace = True)
print("\nCleaned DataFrame:\n", df.to_string())