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

if your_hand == 0:
    if computer_hand == 0:
        print("あいこです")
    if computer_hand == 1:
        print("あなたの勝ちです！")
    if computer_hand == 2:
        print("あなたの負けです")

elif your_hand == 1:
    if computer_hand == 0:
        print("あなたの負けです")
    if computer_hand == 1:
        print("あいこです")
    if computer_hand == 2:
        print("あなたの勝ちです！")

elif your_hand == 2:
    if computer_hand == 0:
        print("あなたの勝ちです！")
    if computer_hand == 1:
        print("あなたの負けです")
    if computer_hand == 2:
        print("あいこです")

else:
    print("不正な入力です")
