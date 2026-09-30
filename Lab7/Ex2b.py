
evens = [2]
num = 2

while evens[-1] < 50:
    num += 2
    evens.append(num)

print(evens)

#method 2 - more efficient
evens = []
for num in range(2, 51, 2):
    evens.append(num)

print(evens)

#while loops are more generalized
#you can use for loops for evertying while loops can do
