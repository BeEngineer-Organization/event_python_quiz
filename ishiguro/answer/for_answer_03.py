n = int(input("好きな整数を入力してください"))

flag = False
for i in range(2, n):
    if n % i == 0:
        flag = True
if flag:
    print("入力された数字は素数ではありません。")
else:
    print("入力された数字は素数です。")
