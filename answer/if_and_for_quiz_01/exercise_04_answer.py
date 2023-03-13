# 数当てゲームをつくりましょう

# 7回チャンスがあるとします。
# 正解の数字が入力した数字より大きければ、「もっと大きいです」と出力
# 正解の数字が入力した数字より小さければ、「もっと小さいです」と出力
# 当たったら「正解」と出力して終了
# 当てられなければ「失敗」と出力
# 5回目の解答の前には、「5で割った余り」をヒントとして出力しましょう
# break と書くと、for文の途中で繰り返しをやめられます

import random

answer = random.randint(0, 1000)

for i in range(7):
    if i == 6:
        hint = answer % 5
        print("5で割った余りは" + str(hint))

    num = int(input("数字を入力してください"))

    if answer > num:
        print("もっと大きいです")
    elif answer < num:
        print("もっと小さいです")
    else:
        print("正解")
        break

    if i == 6:
        print("残念")
