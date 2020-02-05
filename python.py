"""
Вводиться количество слов, затем сами слова, выводится количество слов, которые повторялись.
-----------------------
Sample Input:
4
один
один
два
два
----------
Sample Output:
2
"""

count = int(input())
words = []
for i in range(count):
    words.append(input())

n = 0
for word in words:
    # print('count', word, ' = ', words.count(word))
    if words.count(word) > 1:
        n += 1
        while word in words:
            words.remove(word)

print(n)
