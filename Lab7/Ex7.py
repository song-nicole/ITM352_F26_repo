for number in range(1, 11):
    if number == 8:
        print("Stopping")
        break
    if number != 5:
        print(number)
        continue

#order matters
#if it was flipped, the output would skip 5 and continue to 10