'''
Вася считает числа интересными если сумма первого и последнего разряда числа равны сумме предпоследнего  и последнего.
 Помогите Васе создать программу, которая поможет ему определить интересное число или нет.

Вводятся только трехзначные числа, если число интересное вывести "Интересное" иначе "НЕТ"
'''
a = input()

print("Интересное" if int(a[0])+int(a[2]) == int(a[1])+int(a[2]) else "НЕТ")
