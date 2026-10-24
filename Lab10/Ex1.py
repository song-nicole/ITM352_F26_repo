#Analyze an array of tuples using numpy

import numpy as np # import as -- is a nickname 

#Create an array of tuples of household income and percentiles
hh_income = [
    (10, 14629),
    (20, 25600),
    (30, 37002),
    (40, 50000),
    (50, 63179),
    (60, 79542),
    (70, 100162),
    (80, 130000),
    (90, 184292),
]

hh_income_array = np.array(hh_income) #convert the list of tuples to a numpy array

#Report the dimentions of the array and number of elements in the array
print(f"Dimensions of the array: {hh_income_array.ndim}")
print(f"Number of elements in the array: {hh_income_array.size}")

for i in range(hh_income_array.shape[0]): #loop through the rows of the array
    percentile, income = hh_income_array[i] #unpack the tuple into two variables
    print(f"Percentile: {percentile}, Income: ${income}")

for i in range(hh_income_array.shape[0]): #loop through the rows of the array
    print(hh_income_array[i, 0], hh_income_array[i, 1]) #print the second row of the array - first index is the array, the second is the colums
    