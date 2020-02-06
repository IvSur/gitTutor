"""
Поменять местами самый большой и самый маленький элементы списка, на вход поступает строка из чисел,
возвращаться исправленная строка, как в примере ниже.
Если таких элементов несколько то с первыми которые встретились.
-----------------------
Sample Input:
1 2 3
-----------
Sample Output:
3 2 1
"""

q = input().split()
w = []
for item in q:
    w.append(int(item))

indexMin = w.index(min(w))
indexMax = w.index(max(w))
minItem = w.pop(w.index(min(w)))
maxItem = w.pop(w.index(max(w)))
w.insert(indexMin, maxItem)
w.insert(indexMax, minItem)

for i in w:
    print(i, end=" ")
