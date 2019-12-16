'''
Вводиться три строки в каждой по одному символу,
программа должна вывести сколько кавычек было введено.
'''

a, o, b = input(), input(), input()

print(a+b if oper == "+"
    else a-b if oper == "-"
    else a*b if oper == "*"
    else a/b if oper == "/" and b != 0
    else "Ошибка")
