import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\edenn\Documents\ISTA_131\Final_Project\study_performance.csv')
filtered_data = data[['parental_level_of_education', 'math_score', 'reading_score', 'writing_score']]
average_scores = filtered_data.groupby('parental_level_of_education').mean()
average_scores.plot(kind='barh', figsize=(10, 8))
plt.xlabel('Average Score')
plt.ylabel('Parental Level of Education')
plt.title("Average Math, Reading, and Writing Scores of Students and Their Parental Level of Education")
plt.show()