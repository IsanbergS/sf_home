def read_data():
    data = open('data/war_peace_processed.txt', 'rt', encoding='utf-8').read()
    return data.split('\n')

data = read_data()
target_word = 'князь'
total_number_of_match = 0

for word in data:
    if word == target_word:
        total_number_of_match = total_number_of_match + 1
print(total_number_of_match)
print(data.count('князь'))
