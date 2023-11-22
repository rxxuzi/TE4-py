while True:
    try:
        # ユーザーからの入力を受け取る
        user_input = input()
        # 入力をint型に変換
        user_number = int(user_input)
        break  # 整数が入力されたのでループを終了
    except ValueError:
        # 入力が整数でない場合、もう一度繰り返す
        continue
