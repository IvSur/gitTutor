'''
Вводится одна фраза, выводится эта же фраза в столбик наоборот, как в примере ниже.
'''
str = input()
for i in range(1, len(str)+1):
    print(str[-i])
