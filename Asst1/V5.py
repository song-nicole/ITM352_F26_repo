#Interactive quiz system version 5
#Make a dictionary with the questions and correct answers
#Allow the user to choose the option by its label
#Improve the look and usuability and keep track of correct answers

from string import ascii_lowercase

questions = {
    "What is the capital of France?": ["Paris", "Toulouse", "Nice", "Avignon"],
    "What is the capital of Germany?": ["Berlin", "Munich", "Hamburg", "Cologne"],
    "What is the airspeed of an unladen swallow?": [10, 12, 15, 8],
    "The Last Supper was painted by which artist?": ["da Vinci", "Michelangelo", "Raphael", "Caravaggio"]
}

num_correct = 0

for num, (question, answer) in enumerate(questions.items(), start=1):
    correct_answer = answer[0]  # The first answer in the list is the correct one
    print(f"\nQuestion {num}: {question}")

    sorted_answers = sorted(answer)  # Sort the answers alphabetically
    labeled_answers = dict(zip(ascii_lowercase, sorted_answers))  # Label the answers with letters
    
    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")

    answer_label = input("Choice? ").lower()
    answer = labeled_answers.get(answer_label)

    if answer == correct_answer:
        print("Correct!")
        num_correct += 1
    else:
        print(f"The answer is {correct_answer}, not {answer!r}.")

print(f"\nYou got {num_correct} out of {len(questions)} correct.")