'''
Программа получает на вход два числа A и B, выводит все цифры через запятую от A до B.
'''

a, b = int(input()), int(input())

while a < b:
    print(a, end=", ")
    a += 1

print(b)
