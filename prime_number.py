a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
q = int(a) - 1

while True:
    if int(a) <= 1:
        print("数値が適切ではありません")
        break
    #aに0や負の値が代入されたときにエラーが起きないように修正
    elif q == 1:
        print(a + "は素数である")
        break
    elif int(a) % q == 0:
        print(a + "は素数でない")
        break
    else:
        q -= 1

q = int(b) - 1

while True:
    if int(b) <= 1:
        print("数値が適切ではありません")
        break
    #bに0や負の値が代入されたときにエラーが起きないように修正
    elif q == 1:
        print(b + "は素数である")
        break
    elif int(b) % q == 0:
        print(b + "は素数でない")
        break
    else:
        q -= 1