'''
Вывести на экран циклом N строк из пяти нулей,
причем каждая строка должна быть пронумерована,
программа получает на вход целое положительное число N, должна вывести.
'''

n = int(input())
i = 1
while i <= n:
    print(f'{i}. 0 0 0 0 0')
    i += 1
