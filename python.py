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

n = int(input())
l = []

while n > 0:
    n -= 1
    l.append(int(input()))

print("Цена товаров:")
for str in l:
    print(str)

print()
print("Цена товаров со скидкой:")
for str in l:
    numb = str * 0.9
    if numb % 1 == 0:
        print(int(numb))
    else:
        print(round(numb, 1))
