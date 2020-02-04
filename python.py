"""
Вводиться количество людей, а затем имя каждого человека и его рост ,
программа должна вывести имена всех людей по росту начиная с самого низкого, если рост совпадает,
то выводится в том же порядке как и вносились.
-----------------------
Sample Input:
4
Петр
150
Василий
180
Иван
155
Анна
170
----------
Sample Output:
Петр Иван Анна Василий
"""

count = int(input())
data = {}

while count > 0:
    count -= 1
    words = []
    for i in range(2):
        words.append(input())
    data[words[0]] = words[1]

list_d = list(data.items())
list_d.sort(key=lambda i: i[1])

for item in list_d:
    print(item[0], end=" ")
