# 3つ数字を入力し、それを大きい順に出力してください

num_1 = int(input("1つ目の数字を入力してください"))
num_2 = int(input("2つ目の数字を入力してください"))
num_3 = int(input("3つ目の数字を入力してください"))

# 両端で比較
if num_1 < num_3:
    temp = num_1
    num_1 = num_3
    num_3 = temp

if num_1 < num_2:
    temp = num_1
    num_1 = num_2
    num_2 = temp

if num_2 < num_3:
    temp = num_2
    num_2 = num_3
    num_3 = temp

print(num_1)
print(num_2)
print(num_3)
