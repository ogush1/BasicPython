def prime_number_check(n):
    if n < 1:
        return "数値が適切ではありません"
    q = n - 1
    while True:
        if q == 1:
            return True
        elif q < 0:
            return "数値が適切ではありません"
        elif n % q == 0:
            return False
        else:
            q -= 1

n = float(input("nの値を入力:"))
print(prime_number_check(n))