'''
Напишите программу, которая определяет является ли введенное число простым.
 Если число простое выводиться "<число - простое>" иначе
  "<число> - непростое, есть еще делители: <делители числа через пробел>"
'''
n = int(input())
'''
delits = []
d = 2
while n % d != 0:   # проверяет, является ли число простым, тело цикла не запустится,если число непростое
    d += 1
    delits.append(d)   # ничего не допишется, т.к. если число простое, цикл не выполнится
#    print(delits)
   # print(f'{n} - простое')

print(f'd = {d}')


if d<=2:
    #print(f'd = {d}')
    print(delits)

#print(f'{n} - простое' if (d > 2))
print(f'{n} - простое' if (d > 2) else f'{n} - непростое, есть еще делители: {delits}')

'''
i = 0
flag = 0
delits = []
while i < n:
    i+=1
    if (n%i == 0):
        flag += 1
        delits.append(i)

delits.remove(1)
delits.remove(n)

if flag <= 2:
    print(f'{n} - простое')
else:
    print(f'{n} - непростое, есть еще делители:', end = " ")
    for item in delits:
        print(item, end = " ")


#print(f'{n} - простое' if (flag <= 2) else f'{n} - непростое, есть еще делители: {delits}')

#print(f'Делители: {delits}')
