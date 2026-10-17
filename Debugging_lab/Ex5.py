# Program to remove any scores from a list that are below 50.
 
scores = [60, 45, 30, 85, 10, 90] 

scores_to_return = scores.copy()

for score in scores: 
    if score < 50: 
        scores_to_return.remove(score)

print(scores_to_return) 
