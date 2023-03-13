# パスワード認証をしてください
# パスワードは「BeEngineer」とし
# 入力結果によって、「認証しました」、「アクセス不可」と出力してください

password = input("パスワードを入力してください：")


if password == "beengineer":
    print("認証しました")
else:
    print("アクセス不可")
