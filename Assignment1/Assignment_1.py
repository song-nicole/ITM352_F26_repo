# Name: Nicole Song
# Date: Oct. 7, 2026

# Create a quiz that asks the user at least 5 multiple choice questions and present at least 4 options
# Requiremnt 1: Write the history of scores out to a file
# Requiremnt 2: Add a 50/50 feature that eliminates 2 incorrect answers from the options (this feature can only be used once per quiz)

from string import ascii_lowercase
import random
import json

question_file = open("questions.json", "r")
questions = json.load(question_file)

scores = []

QUESTIONS_PER_QUIZ = 5

num_questions = min(QUESTIONS_PER_QUIZ, len(questions))
selected_questions = random.sample(list(questions.items()), num_questions)

input("\nWelcome to the Hawaii Quiz! Press 'Enter' to begin. ")
print("\nYou will be asked 5 questions about Hawaii.")
print("\nTip! You can type 'hint' to eliminate 2 incorrect answers from the options.\n   *The 50/50 feature can only be used once per quiz.")
input("\nPress 'Enter' to start the quiz. ")

def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


def get_answer(question, alternatives):
    labeled_answers = dict(zip(ascii_lowercase, alternatives))
    global hint

    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")
        
    while (answer_label := input("Your answer: ").lower()) not in labeled_answers:
        if answer_label == "hint" and hint == False:
            hint = True
            incorrect_answers = [ans for ans in alternatives if ans != correct_answer]
            eliminated_answers = random.sample(incorrect_answers, 2)
            print("\nHint: The following options have been eliminated:")
            for eliminated in eliminated_answers:
                print(f"- {eliminated}")
            print()
            continue
        elif answer_label == "hint" and hint == True:
            print("You have already used the 50/50 feature. You cannot use it again.")
            continue
        else:
            print(f"Invalid choice. Please select one of {', '.join(labeled_answers.keys())}.")

    answer = labeled_answers.get(answer_label)
    return labeled_answers[answer_label]

# Function to ask a question and check the answer
def ask_question(question, alternatives):
    global correct_answer
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))
    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"The answer is '{correct_answer!r}', not {answer!r}.")
        return 0

# Ask user if they want to play again
def play_again():
    replay = input("Would you like to play again? (y/n): ").lower()
    if replay == "y":
        print("\nStarting a new game...")
        operate()
    elif replay == "n":
        print("Thank you for playing!")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        play_again()

# Ask user if they want to see their past scores
def score_history():
    past_scores = input("\n \nWould you like to see your past scores? (y/n): ").lower()
    if past_scores == "y":
        print("Your past scores are:")
        for score in scores:
            print(score)
        play_again()
    elif past_scores == "n":
        play_again()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        score_history()

# Main program logic starts here
questions = prepare_questions(questions, QUESTIONS_PER_QUIZ)

# Main Loop
def operate():
    num_correct = 0
    global hint
    hint = False

    for num, (question, answers) in enumerate(questions, start=1):
        print(f"\nQuestion {num}: {question}")
        num_correct += ask_question(question, answers)

    print(f"\nYou got {num_correct} correct.")
    scores.append(num_correct)

    score_history()

operate()