"""
Необходимо определить, начинается ли слово с 123.
 Слова вводятся через пробелы.
 Вывести ответ рядом либо True, либо False, как в примере ниже.
-----------------------
Sample Input:
123 321123 123456789 111
----------
Sample Output:
123 True
321123 False
123456789 True
111 False
"""

txt = input().split()

for str in txt:
    if str.find("123"):
        print(str + " False")
    else:
        print(str + " True")



