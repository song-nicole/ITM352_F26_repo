#Read a json file of taxi trip data and create a data frame and some simple stats
import pandas as pd

#Read the json file into a pandas dataframe
df = pd.read_json("Taxi_Trips.json")

print(df.head(6)) #print the first few rows of the dataframe (raw data) (default is first 5 rows)

print(df.describe()) #print some simple statistics about the dataframe

median = df["fare"].median()
print("The median fare value is: ",median)
