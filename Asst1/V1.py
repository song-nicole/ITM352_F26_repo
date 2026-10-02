#First version of quiz game
#Name: Nicole Song
#Date: Oct. 2, 2026

answer = input("What is the capital of France? ")
if answer == "Paris":
    print("Correct!")
else:
    print(f"The answer is Paris, not {answer!r}.")
    #!r puts it in it's raw format

answer = input("What is the capital of Germany? ")
if answer == "Berlin":
    print("Correct!")
else:
    print(f"The answer is Berlin, not {answer!r}.")