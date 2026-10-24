#Create a pandas dataframe from individual lists
#Do some simple stats on the data

import pandas as pd

#List of individuals and their names, ages, and genders
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

raw_data = zip(ages, gender)

# Creata a pandas dataframe from the list
df = pd.DataFrame(data=raw_data, index=names, columns=["Age", "Gender"]) #Think of a dataframe as a spreadsheet in memory

summary = df.describe() #get summary stats on the data (count, mean, std, min, 25%, 50%, 75%, max)
print(summary)

#Calculate average by gender
average_age_by_gender = df.groupby("Gender").mean() #group the data by gender and calculate the mean age for each group
print("\nAverage age by gender:")
print(average_age_by_gender)