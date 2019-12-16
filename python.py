'''
Дано три числа. Найти количество положительных чисел среди них;
'''

n = 0

for i in range(3):
    if int(input()) > 0:
        n +=1
#    print("qqqqq")

'''
if int(input()) > 0:
    n +=1

if int(input()) > 0:
    n +=1

if int(input()) > 0:
    n +=1
'''

print("n =", n)
