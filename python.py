'''
Программа получает на вход фразу из нескольких слов, выводит фразу без первого слова.
'''
n = 0
str = input().split()
for i in range(1, len(str)):
    print(str[i], end=" ")
