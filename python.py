'''
Напишите программу, которая получает на вход одно целое число N и
выводит полквадрата из звездочек (*) N*N, как в примере ниже.
'''
s = 0
for i in range(int(input()) - 1):
    s += 1
    for j in range(s):
        print("*", end=" ")
    print()
