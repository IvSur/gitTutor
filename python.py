"""
Напишите программу, которая получает данные о полете самолета с датчика высоты каждую секунду,
известно что полет является завершенным когда высота равна 0.
Программа получает показания и должна вывести на какой секунде полета самолет достиг максимальной высоты.
-----------------------
Sample Input:
1
2
3
2
1
0
----------
Sample Output:
3
"""

q = []
while True:
    q.append(int(input()))
    if 0 in q:
        break

print(q.index(max(q)) + 1)
