# Name: Nicole Song
# Date: Oct. 7, 2026

# Create a quiz that asks the user at least 5 multiple choice questions and present at least 4 options
# Requiremnt 1: Write the history of scores out to a file
# Requiremnt 2: Add a 50/50 feature that eliminates 2 incorrect answers from the options (this feature can only be used once per quiz)

from string import ascii_lowercase
import random

questions = {
    "What is the name of the tallest mountain in Hawaii?": ["Mauna Kea", "Koko Head", "Mauna Loa", "Kamakou", "Kawaikini"],
    "What is Hawaii's state flower?": ["Yellow Hibiscus", "Plumeria", "Bird of Paradise", "Purple Orchid"],
    "Which of the following is a native species in Hawaii?": ["White Tern", "Mongoose", "Chicken", "Gecko", "Myna Bird"],
    "What is a popular resturant in the US that doesn't exist in Hawaii?": ["In-N-Out Burger", "Chick-fil-A", "Olive Garden", "Subway", "Wendy's"],
    "Which is the largest mall in Hawaii?": ["Ala Moana Center", "Pearlridge Center", "Kahala Mall", "Windward Mall", "Royal Hawaiian Center"],
}

scores = []

QUESTIONS_PER_QUIZ = 5

num_questions = min(QUESTIONS_PER_QUIZ, len(questions))
selected_questions = random.sample(list(questions.items()), num_questions)

num_correct = 0

input("Welcome to the Hawaii Quiz! Press 'Enter' to begin. ")

# Number the questions starting from 1
for num, (question, answer) in enumerate(questions.items(), start=1):
    correct_answer = answer[0]  # The first answer in the list is the correct one
    print(f"\nQuestion {num}: {question}")

    # Sort the answers alphabetically
    sorted_answers = sorted(answer)
    # Label the answers with letters and randomize their order
    labeled_answers = dict(zip(ascii_lowercase, random.sample(sorted_answers, k=len(sorted_answers))))
    
    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")

    # Ensure the user selects a valid answer label that's within range
    while (answer_label := input("Your answer: ").lower()) not in labeled_answers:
        print(f"Invalid choice. Please select one of {', '.join(labeled_answers.keys())}.")

    answer = labeled_answers.get(answer_label)

    # Check if user's answer is correct
    if answer == correct_answer:
        print("Correct!")
        num_correct += 1
    else:
        print(f"The answer is {correct_answer}, not {answer!r}.")

print(f"\nYou got {num_correct} out of {len(questions)} correct.")
scores.append(num_correct)

# Ask user if they want to play again
def play_again():
    replay = input("Would you like to play again? (y/n): ").lower()
    if replay == "y":
        print("Starting a new game...")
    elif replay == "n":
        print("Thank you for playing!")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        play_again()

# Ask user if they want to see their past scores
def score_history():
    past_scores = input("Would you like to see your past scores? (y/n): ").lower()
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

score_history()
