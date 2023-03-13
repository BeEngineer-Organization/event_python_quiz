#フィボナッチ数列を10個まで表示してください
#どの数字も前２つの数字を足した数字「1, 1, 2, 3, 5, 8, 13, 21,,,,」です

a = 0
b = 1

# #1
for i in range(10):
    print(b)
    c = a + b
    a = b
    b = c

#2
for i in range(10):
    print(b)
    a, b = b, a + b