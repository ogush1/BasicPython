a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO

a = int(a)
b = int(b)
r = a % b

while not r == 0:
    q = a // b
    r = a % b
    a = b
    b = r

print("最大公約数は" + str(a))