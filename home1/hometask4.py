import re
import math

def read_data():
    with open('data/war_peace_processed.txt', 'rt', encoding='utf-8') as f:
        data = f.read()
    return data.split('\n')

data = read_data()

# Объединяем строки для разделения на главы
result = " ".join(data)
chapters = result.split("[new chapter]")
total_number_of_chapters = len(chapters)
print(total_number_of_chapters)
unique_in_chapter = 0
target_word = 'анна'
target_chapter = 4


# Регулярное выражение для точного совпадения слова 'человек'
pattern = re.compile(rf'\b{target_word}\b', re.IGNORECASE)

for chapter in chapters:
    # Приводим к нижнему регистру и ищем точные вхождения слова "человек"
    if pattern.search(chapter):
        unique_in_chapter += 1
# Подсчёт document frequency (df)
df = unique_in_chapter / total_number_of_chapters
print(unique_in_chapter)
print(df)


data = read_data()

# Объединяем строки для разделения на главы
result = " ".join(data)
chapters = result.split("[new chapter]")
total_number_of_chapters = len(chapters)

# Регулярное выражение для точного совпадения слова 'человек'
pattern = re.compile(rf'\b{target_word}\b', re.IGNORECASE)
chapter_text = chapters[target_chapter]

total_words_in_chapter = len(chapter_text.split())
print(total_words_in_chapter)
matches = pattern.findall(chapter_text)

tf = len(matches)/total_words_in_chapter
print(tf)

tf_idf = math.log(1 + tf) * math.log(1/df)
print(tf_idf)