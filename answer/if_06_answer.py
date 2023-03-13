# 便利機能を使う宣言
import time
import random

# カウントダウン
print("5秒以内に数字を入力してください")
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)

# 答えの数字をランダムに作成
num = int(random.random() * 1000000)
print(num)

# 開始時間を計測
start = time.time()

# 入力を求める
input_num = int(input("数字を入力してください："))

# 入力後の時間を計測
end = time.time()

# 入力後の時間と開始時間の引き算から、
# 入力にかかった時間を計測
time = end - start

# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝ #
# 答えの判定のコードを書いてみよう！ #
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝ #

# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝　ロジック　＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝ #
# 　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　 #
# 　　正解の数字と入力した数字が一致するーーーーーーーーーーーーーーー　　　　 #
# 　　　　｜　　　　　　　　　　　　　　　　　　　　　　　　　　　　｜　　　　 #
# 　　　　｜〇　　　　　　　　　　　　　　　　　　　　　　　　　　　｜　　　　 #
# 　　　　｜　　　　　　　　　　　　　　　　　　　　　　　　　　　　｜　　　　 #
# 　　かかった時間が５秒以内ーーーーーーーー　　　　　　　　　　　　｜　　　　 #
# 　　　　｜　　　　　　　　　　　　　　　｜　　　　　　　　　　　　｜　　　　 #
# 　　　　｜〇　　　　　　　　　　　　　　｜✕　　　　　　　　　　　｜✕　　　　#
# 　　　　｜　　　　　　　　　　　　　　　｜　　　　　　　　　　　　｜　　　　 #
# 　　「成功！」と表示　　　「正解！でも遅い、、」と表示　　　「失敗」と表示　 #
# 　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　 #
# 　　結果に関わらず、かかった時間も表示する。                              #
# 　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　 #
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝ #


if num == input_num:
    if time < 5:
        print("成功！")
    else:
        print("正解！でも遅い、、")
else:
    print("失敗")


print(time, "秒")
