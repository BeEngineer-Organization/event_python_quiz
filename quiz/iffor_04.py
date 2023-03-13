# 数当てゲームをつくりましょう

# 7回チャンスがあるとします。
# 正解の数字が入力した数字より大きければ、「もっと大きいです」と出力
# 正解の数字が入力した数字より小さければ、「もっと小さいです」と出力
# 当たったら「正解」と出力して終了
# 当てられなければ「失敗」と出力
# break と書くと、for文の途中で繰り返しをやめられます

# 〜〜追加課題〜〜
# 7回目の最後の解答の前には、「5で割った余り」をヒントとして出力しましょう

import random

#0以上999以下のランダムな数字
answer = random.randint(0, 1000)

#入力してもらうコードは以下のようにしましょう
num = int(input("数字を入力してください"))