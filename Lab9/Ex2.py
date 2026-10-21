# read a csv file containing window cleaning employee data and compute salary statistics
# print info about file statistics and permissions before reading the file

import csv
import os

#check if the file exists and is readable
if not os.path.isfile("window_cleaning_company.csv"):
    print("File does not exist.")
    exit(1)

if not os.access("window_cleaning_company.csv", os.R_OK):
    print("File is not readable.")
    exit(1)
else:
    file_size = os.path.getsize("window_cleaning_company.csv")
    print(f"File exists and is readable. Size: {file_size} bytes")

csv_filename = "window_cleaning_company.csv"
salaries = []

# Read the CSV file and store the salaries in a list
with open(csv_filename, "r") as csv_file:
    reader = csv.reader(csv_file) #reads the scv file
    headers = next(reader) #skips the first row of the csv file
    print("Headers:", headers)
    salary_index = headers.index("Annual_Salary") #finds the index of the salary column
    for row in reader:
        salary = float(row[salary_index])
        salaries.append(salary)

    #Compute salary stats
    average_salary = sum(salaries) / len(salaries)
    min_salary = min(salaries)
    max_salary = max(salaries)

    # Print the salary stats
    print(f"Average Salary: ${average_salary:.2f}")
    print(f"Minimum Salary: ${min_salary:.2f}")
    print(f"Maximum Salary: ${max_salary:.2f}")
