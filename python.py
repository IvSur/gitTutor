'''
Напишите программу которая получает на вход одну фразу и печатает ее как в примере ниже.
П
 р
  и
   в
    е
     т
'''
str = input()

for i in range(len(str)):
    print(" " * i, end = "")
    print(str[i::len(str)])
