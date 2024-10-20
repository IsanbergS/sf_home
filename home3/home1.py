import pandas as pd


lectures_df = pd.read_csv('home3/lectures.csv')
train_df = pd.read_csv('home3/train_part_0.csv')

unique_lecture = train_df['content_id'].nunique()
unique_lecture = lectures_df['lecture_id'].unique()
print(unique_lecture)
#unique_tag = lectures_df['part'].nunique()
# Подсчет количества уникальных элементов с определенным значением part
#part_value = 1  # Здесь можно указать нужное значение part
#unique_elements_for_part = lectures_df[lectures_df['part'] == part_value].nunique()
#print(f'Количество уникальных элементов для part = {part_value}: {unique_elements_for_part}')
