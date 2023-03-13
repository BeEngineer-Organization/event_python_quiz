# 3つ数字を入力し、それを大きい順に出力してください

num_1  = int(input("1つ目の数字を入力してください"))
num_2 = int(input("2つ目の数字を入力してください"))
num_3 = int(input("3つ目の数字を入力してください"))

# 解答1
# 両端で比較
if num_1 < num_3:
    num_1, num_3 = num_3, num_1

# 真ん中と両端を比較
if num_1 < num_2:
    num_1, num_2 = num_2, num_1
elif num_2 < num_3:
    num_2, num_3 = num_3, num_2

print(num_1)
print(num_2)
print(num_3)

# 解答2
# 先頭から比較
if num_1 < num_2:
    num_1, num_2 = num_2, num_1
if num_2 < num_3:
    num_2, num_3 = num_3, num_2
if num_1 < num_2:
    num_1, num_2 = num_2, num_1

print(num_1)
print(num_2)
print(num_3)