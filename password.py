password = "a123456"
i = 3

while i >= 0:
    i = i-1
    test = input("請輸入密碼:")
    if password == test:
        print("登入成功")
        break
    else:
        if i == 0:
            print("沒機會嘗試了")
            break
        print("密碼錯誤! 還有", i, "次機會")
