import pandas as pd

data = {
    'Student_ID': [1, 2, 3, 4, 5],
    'Course': ['Math', 'Science', 'Math', 'Science', 'History'],
    'Score': [85, 78, 92, 80, 70],
    'Hours_Studied': [10, 12, 15, 9, 8]
}
student_data = pd.DataFrame(data)
# 1
correlation_per_course = student_data.groupby('Course')[['Hours_Studied', 'Score']].corr().iloc[0::2, -1]

# 2
strongest_corr_course = correlation_per_course.idxmax()
weakest_corr_course = correlation_per_course.idxmin()

print("Correlation coefficient between Hours_Studied and Score for each course:")
print(correlation_per_course)

print("\nCourses with the strongest correlation:")
print(strongest_corr_course)
print("\nCourses with the weakest correlation:")
print(weakest_corr_course)

# 3
average_data = student_data.groupby('Course')[['Score', 'Hours_Studied']].mean()
print("\nAverage score and hours studied for each course:")
print(average_data)
           
