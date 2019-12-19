'''
Напишите программу, которая получает на вход одно целое число N и выводит квадрат из звездочек (*) N*N.
'''
n = int(input())

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
