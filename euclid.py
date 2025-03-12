# 問3
a = input("a の値を入力: ")
b = input("b の値を入力: ")

a = int(a)
b = int(b)

def euclid(a,b):
    while True:
        q = a // b
        r = a % b
        a = b
        b = r
        if r == 0:
            return a

print(euclid(a,b))

# 問4
a = input("a の値を入力: ")
b = input("b の値を入力: ")

a = int(a)
b = int(b)

def euclid(a,b):
    while True:
        q = a // b
        r = a % b
        a = b
        b = r
        if r == 0:
            if a == 1:
                return True
            else:
                return False
print(euclid(a,b))

# Extra
import random

p = 0
S = 0
for i in range(100000):
    a = random.randint(1,10000)
    b = random.randint(1,10000)
    if euclid(a,b) == True:
        S += 1
    else:
        S += 0
p = S / 100000
print(p)