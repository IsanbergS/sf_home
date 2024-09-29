import re
import math
from collections import defaultdict

def read_data():
    with open('data/war_peace_processed.txt', 'rt', encoding='utf-8') as f:
        data = f.read()
    return data.split('\n')

data = read_data()

# Объединяем строки для разделения на главы
result = " ".join(data)
chapters = result.split("[new chapter]")
total_number_of_chapters = len(chapters)


target_word = 'анна'
target_chapter = 4

chapter_text = chapters[target_chapter]
words_in_target_chapter = chapter_text.split()
statistic_array = []
word_freq = defaultdict(float)
# Регулярное выражение для точного совпадения слова 'человек'



unique_words_in_target_chapter = list(set(words_in_target_chapter))
# print(len(unique_words_in_target_chapter))

for i,word in enumerate(unique_words_in_target_chapter):
    target_word = word
    pattern = re.compile(rf'\b{target_word}\b', re.IGNORECASE)
    # print(i)
    
    chapters_with_target_word = 0
    for chapter in chapters:
        # Приводим к нижнему регистру и ищем точные вхождения слова "человек"
        if pattern.search(chapter):
            chapters_with_target_word += 1
    # Подсчёт document frequency (df)
    df = chapters_with_target_word / total_number_of_chapters

    # print(df)



    total_words_in_chapter = len(words_in_target_chapter)

    matches = pattern.findall(chapter_text)
    total_target_word_in_chapter = len(matches)
    #target word frequency
    tf = total_target_word_in_chapter/total_words_in_chapter


    tf_idf = math.log(1 + tf) * math.log(1/df)
    # print(tf_idf)
    word_freq[word] = tf_idf
sorted_list = dict(sorted(word_freq.items(), key = lambda item: (item[1], item[0]), reverse=True))
first_4_items = list(sorted_list.keys())[:3]
print(*first_4_items)