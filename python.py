'''
Даны целые неотрицательные числа a, b, c, d, при этом 0≤c<d.
 Выведите в порядке возрастания все числа от a до b, которые дают остаток c при делении на d.
'''
#a, b, c, d = int(input()), int(input()), int(input()), int(input())
a = []

for i in range(4):
    a.append(int(input()))

for item in range(a[0], a[1]+1):
    if item % a[3] == a[2]:
        print(item, end = " ")
