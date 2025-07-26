"""Given the participant's score sheet for your University Sports Day, 
you are required to find the runner-up score. You have scores. Store them in a list 
and find the score of the runner-up."""

#code
n = int(input("Enter number of participants: "))

scores = list(map(int, input("Enter the scores: ").split()))

unique_scores = list(set(scores))
unique_scores.sort(reverse=True)

if len(unique_scores) >= 2:
    print("Runner-up score:", unique_scores[1])
else:
    print("Not enough participants to determine a runner-up.")
