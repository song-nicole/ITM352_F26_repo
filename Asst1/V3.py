#Interactive quiz system version 3
#Make a dictionary with the questions and correct answers

questions = {
    "What is the capital of France?": ["Paris", "Toulouse", "Nice", "Avignon"],
    "What is the capital of Germany?": ["Berlin", "Munich", "Hamburg", "Cologne"],
    "The Last Supper was painted by which artist?": ["da Vinci", "Michelangelo", "Raphael", "Caravaggio"]
}

for question, answer in questions.items():
    correct_answer = answer[0]  # The first answer in the list is the correct one
    for answer in answer:
        print(f"- {answer}")

    answer = input(f"{question} ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer}, not {answer!r}.")
        