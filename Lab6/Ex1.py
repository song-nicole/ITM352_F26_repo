emotions = ("happy", "sad", "fear", "surprise")

is_it_true = emotions[-1] == "happy" and len(emotions) > 3
#single = sign is for assignment
#double == sign is for comparison

print(is_it_true)

#Method 1
print(emotions[-1] == "happy" and len(emotions) > 3)

#Method 2
if len(emotions) > 3 and emotions[-1] == "happy":
    print(True)
else:
    print(False)