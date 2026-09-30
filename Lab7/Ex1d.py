#Use list comprehensive to create a list of odd numbers from 1 to 50

# list comprehension = [expression for item in iterable  if condition]

odd_nums = [2*num+1 for num in range(0, 25)]
print(odd_nums)

#this version is less efficient because you're generating more numbers and using an additional if statement
odd_nums = [2*num+1 for num in range(0, 50) if 2*num+1 <= 50]
print(odd_nums)