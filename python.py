"""
Напишите программу, которая получает на вход сначала количество слов, затем сами слова.
Выводит список с количеством букв в каждом слове и затем слово в котором больше всего букв,
если таких слов несколько то первое, которое встретилось.
-----------------------
Sample Input:
3
один
два
три
----------
Sample Output:
4
3
3
один
"""

countWords = int(input())
words = []
countLetters = 0
wordXXL = ""

while countWords > 0:
    countWords -= 1
    words.append(input())

for word in words:
    print(len(word))
    if countLetters < len(word):
        countLetters = len(word)
        wordXXL = word

print(wordXXL)
