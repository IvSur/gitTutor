'''
У Коли есть младшая сестра, которая еще не умеет считать.
 Необходимо написать программу, которая поможет сестре Коли научиться считать.
 Вводиться цифры от 1 до 5, если во время ввода была ошибка и числа были не по порядку,
 все начинается сначала, пока правильно не будет введена последовательность от 1 до 5.
 Если все числа введены правильно выводиться "Молодец, ты научилась считать до 5" и количество введенных цифр.
'''
n = 0
numbers = [1, 2, 3, 4, 5]
str = []
while True:
    n+=1
    str.append(int(input()))
    if str == numbers:
        print("Молодец, ты научилась считать до 5")
        print(n)
        continue

'''
    print(f'str = {str}')
    print(str == numbers)
    if n > 5:
        break
'''
