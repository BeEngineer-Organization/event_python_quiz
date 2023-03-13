# 合否を判定するプログラム
# 数学は65点以上、国語は80点以上、英語は70点以上で合格と出力してください

subject = input("科目を入力してください(数学・国語・英語):")
point = int(input("点数を入力してください:"))
print(subject + "：" + str(point) + "点")

if subject == "数学":
    if point >= 65:
        print("合格")
    else:
        print("不合格")
elif subject == "国語":
    if point >= 80:
        print("合格")
    else:
        print("不合格")
else:
    if point >= 70:
        print("合格")
    else:
        print("不合格")
