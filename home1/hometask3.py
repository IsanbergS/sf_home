import re

def read_data():
    with open('data/war_peace_processed.txt', 'rt', encoding='utf-8') as f:
        data = f.read()
    return data.split('\n')

data = read_data()

# Объединяем строки для разделения на главы
result = " ".join(data)
chapters = result.split("[new chapter]")
total_number_of_chapters = len(chapters)

target_word = 'человек'
target_chapter = 15

# Регулярное выражение для точного совпадения слова 'человек'
pattern = re.compile(rf'\b{target_word}\b', re.IGNORECASE)
chapter_text = chapters[target_chapter]

total_words_in_chapter = len(chapter_text.split())

matches = pattern.findall(chapter_text)

tf = len(matches)/total_words_in_chapter
print(tf)