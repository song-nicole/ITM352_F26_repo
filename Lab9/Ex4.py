#Calculate the total of all fares, average fare, and the max trip distance for those greater than $10

import csv

filename = "taxi_1000.csv"

with open(filename, 'r') as file:
    csv_reader = csv.reader(file)
    max_distance = 0.0
    average_fare = 0.0
    num_rows = 0

    for row in csv_reader:
        if num_rows == 0: #skip the header row - only happens once for the first row
            fare_index = row.index("Fare") #find the index of the fare column
            distance_index = row.index("Trip Miles") #find the index of the distance column
            num_rows += 1
            continue

        if num_rows > 0:
            fare = float(row[fare_index])
            distance = float(row[distance_index])
            if fare > 10:
                total_fare += fare
                if distance > max_distance:
                    max_distance = distance

        num_rows += 1

if num_rows > 1: # check if there are any data rows to avoid division by zero
    average_fare = total_fare / (num_rows - 1) # subtract 1 to exclude the header row

print(f"Total Fare: ${total_fare:.2f}")
print(f"Average Fare: ${average_fare:.2f}")
print(f"Max Trip Distance: {max_distance:.2f} miles")