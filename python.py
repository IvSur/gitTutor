'''
У каждого из нас есть мобильный телефон и у каждого он разный.
А именно отличается то сколько букв может вместить один экран в одну строку.
 Напишите программу которая преобразует строку в зависимости от способности телефона.

Вводится строка и то сколько букв умещается на экран телефона.

Выводится преобразованная строка.
-----------
Sample Input:

Привет как дела?
5
Sample Output:

Приве
т как
 дела
?
'''
str, n = input(), int(input())

for j in range(0, len(str), n):
    for i in range(j, n+j):
        if i < len(str):
            print(str[i], end = "")
    print()
