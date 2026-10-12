Name: Nicole Song
Last update: October 11, 2026

● Data Structure Justification: What data structure design was used to store the quiz questions and why is the best for the application? Explain the design quality goals for this? E.g. readability by human, easy to read from a file, etc. Do not simply list the goals. Explain them relative to storing quiz questions.

A dictionary is used because it ensures that the questions and the answer options are stored together. The key value pairs help with organization, allowing you to easily keep track of which questions are associated with which answer options. It allows both the human reader and the computer to instantly see the question and the associated answers without needing to search through the entire program. In addition, it is also formatted like a traditional multiple choice quiz that many are familiar with.

● Function Design: Why did you design your non-trivial custom function the way you did, and what specific problem does it solve in the application?

I designed the functions the way I did because it acts as a loop that continously runs as it is called on. For example, the "play_again" function asks the user if they would like to replay the quiz game. By incorporating the function within itself, it can repeatedly reprompt the user until it receives a satisfactory input. Instead of reentering the question, the function can simply loop itself. Similarily, the "score_history" function shows the user their past scores and can also loop repeatedly like the "play_again" function.

● Control Flow: A brief explanation of how the application handles invalid user inputs (e.g., preventing inputs outside of "a-d") and why you chose that validation loop structure. Explain the design quality goals for this? E.g. Do not simply list the goals. Explain them relative to storing quiz questions[RK1].

The way this program handles invalid inputs is simple. It first uses if statements to check if the input is valid and if it isn't, it'll send a short message explaining the error in addition to a message reprompting the user to enter a valid input. This cycle will essentially continue until a qualified input is received. I chose this loop structure because it's simple and removes the need to repeat user prompts within the code. It is incorporated with a function instead of a for loop or while loop because it relies heavily on user input.

● Use of AI: You must also include a statement on how you used AI (Copilot or any other tool) in the creation of this assignment. Be honest: if we ask you to explain your code and you cannot, that will mean that you relied too heavily on AI.

I used copilot to understand the foundational code introduced in the assignment 1 workshop. There were a few sections where I felt confused or uncertain, so I used copilot to understand why certain functions were formated the way they are and what they do. I also used copilot to find the right placement for "global eliminate" and "eliminate = False" to properly incorporate the 50/50 feature so that it is only used once per quiz round. I used AI to learn more about using JSON files, especially about how to add and take out information from those files. Finally, I used AI to learn how to incorporate images to the quiz questions.