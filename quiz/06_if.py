# PC とじゃんけんしよう

# PC はランダムで手を選びます。
# グー：0、チョキ：1、パー：2という値に対応しています。
# 0、１、２以外の数字が入力された場合は「不正な入力です。」と出力します。

import random


def parse_number_to_hand(num):
    if num == 0:
        return "グー"
    elif num == 1:
        return "チョキ"
    elif num == 2:
        return "パー"
    else:
        print("不正な入力です")


print("グー：0、チョキ：1、パー：2")

your_hand = int(input("あなたの手を半角数字で入力してください："))
computer_hand = random.randint(0, 2)

print("あなたの手：", parse_number_to_hand(your_hand))
print("コンピュータの手：", parse_number_to_hand(computer_hand))

# ここから書く
