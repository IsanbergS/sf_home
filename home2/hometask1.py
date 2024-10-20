import pandas as pd

# Загрузка данных (если данные уже загружены, этот шаг можно пропустить)
file_path = 'home2\students_performance.csv'
student_data = pd.read_csv(file_path)
# Расчет среднего значения балла по письму
average_writing_score = student_data['math score'].mean()
column_names = student_data.columns
most_common_race_group = student_data['race/ethnicity'].value_counts().idxmax()
average_reading_score_prep_course = student_data[student_data['test preparation course'] == 'completed']['reading score'].mean()

average_reading_score_prep_course = student_data[student_data['math score'] == 0].shape[1]
print(average_reading_score_prep_course)
print(column_names)
print(average_reading_score_prep_course)
unique_values = student_data['test preparation course'].unique()

print(unique_values)

mean_with_pay = student_data[student_data['lunch'] == 'standard']['math score'].mean()
mean_without_pay = student_data[student_data['lunch'] == 'free/reduced']['math score'].mean()
print(mean_with_pay)
print(mean_without_pay)

parents_education_column = student_data['parental level of education'].unique()
print(parents_education_column)
num_of_children_with_educated_parents = student_data[student_data['parental level of education'] == 'bachelor\'s degree'].shape[0]
print(student_data.shape[0])
print(num_of_children_with_educated_parents)

median_writing_A = student_data[student_data['race/ethnicity'] == 'group A']['writing score'].median()
median_writing_C = student_data[student_data['race/ethnicity'] == 'group C']['writing score'].median()
print(median_writing_A-median_writing_C)

print(student_data.info())