a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
q = int(a) - 1

while True:
    if q == 1:
        print(a + "は素数である")
        break
    elif int(a) % q == 0:
        print(a + "は素数でない")
        break
    else:
        q -= 1

q = int(b) - 1

while True:
    if q == 1:
        print(b + "は素数である")
        break
    elif int(b) % q == 0:
        print(b + "は素数でない")
        break
    else:
        q -= 1