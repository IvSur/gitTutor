'''
Программа получает на вход одну фразу и если в этой фразе есть описание половины чего-либо,
умножает на два. Как в примере ниже.
'''
str = input()

if str[:4] == "пол-":
    print(str.lower().replace("пол-", "два "))
if str[:4] == "пол ":
    print(str.lower().replace("пол ", "два "))
elif str[:3] == "пол":
    print(str.lower().replace("пол", "два "))
elif " пол-" in str:
    print(str.lower().replace(" пол-", " два "))
elif " пол " in str:
    print(str.lower().replace(" пол ", " два "))
elif " пол" in str:
    print(str.lower().replace(" пол", " два "))
else:
    print(str)
