"""
Программа получает на вход количество цифр, затем сами цифры,
выводит список этих цифр в той же последовательности, как они вносились.
-----------------------
Sample Input:
5
6
1
7
0
4
5
----------
Sample Output:
[1, 2, 3, 4, 5]
"""

n = int(input())
l = []

while n > 0:
    n -= 1
    l.append(int(input()))

l.sort(reverse=True)
print(l)
