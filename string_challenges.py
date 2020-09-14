# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))

from collections import Counter
# Вывести количество гласных букв в слове
voice = ["а", "о", "у", "и", "е", "ы", "э", "я"]
word = 'Архангельск'
number = 0

for letter in word.lower():
    if letter in voice:
        number += 1
        
print(number)

letter_counts = {}
for letter in word.lower():
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова
sentence = 'Мы приехали в гости'

new_sent = sentence.replace(" ",'')

print(len(new_sent)/ len(sentence))
