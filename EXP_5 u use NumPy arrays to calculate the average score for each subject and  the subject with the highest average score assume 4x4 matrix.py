import numpy as np

student_scores = np.array([
    [80, 75, 85, 90],  
    [70, 85, 90, 88],  
    [90, 88, 82, 78], 
    [95, 92, 87, 84]   
])

average_scores = np.mean(student_scores, axis=0)

subject_with_highest_avg_score = np.argmax(average_scores)
highest_avg_score = average_scores[subject_with_highest_avg_score]

subjects = ['Math', 'Science', 'English', 'History']

print("Average score for each subject:")
for i, subject in enumerate(subjects):
    print(f"{subject}: {average_scores[i]}")

print(f"\nThe subject with the highest average score is {subjects[subject_with_highest_avg_score]} "
      f"with an average score of {highest_avg_score}.")
