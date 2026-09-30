#method 1 - continues checking until 99
for num in range(1, 51):
    value = 2 * num - 1
    if value <= 50:
        print(value)

#method 2 - breaks the loop once the value exceeds 50
for num in range(1, 51):
    value = 2 * num - 1
    if value > 50:
        break
    else:
        print(value)

#method 3
for num in range(1, 26):
    value = 2 * num - 1
    print(value)
    