emotions = ("happy", "sad", "fear", "surprise")

is_it_true = emotions[-1] == "happy" and len(emotions) > 3
#single = sign is for assignment
#double == sign is for comparison

print(is_it_true)
print(emotions[-1] == "happy" and len(emotions) > 3)

if len(emotions) > 3 and emotions[-1] == "happy":
    print(True)
else:
    print(False)