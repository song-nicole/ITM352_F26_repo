#Interactive quiz system version 4
#Make a dictionary with the questions and correct answers
#Allow the user to choose the option by its label

questions = {
    "What is the capital of France?": ["Paris", "Toulouse", "Nice", "Avignon"],
    "What is the capital of Germany?": ["Berlin", "Munich", "Hamburg", "Cologne"],
    "The Last Supper was painted by which artist?": ["da Vinci", "Michelangelo", "Raphael", "Caravaggio"]
}

for question, answer in questions.items():
    correct_answer = answer[0]  # The first answer in the list is the correct one
    sorted_answers = sorted(answer)  # Sort the answers alphabetically
    
    for label, answer in enumerate(sorted_answers, start=1):
        print(f"{label}. {answer}")

    answer_label = int(input(f"{question} "))
    answer = sorted_answers[answer_label - 1]

    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer}, not {answer!r}.")

