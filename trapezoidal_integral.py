from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
from math import pi
a = 0
b = pi / 2
N = 100
h = (b - a) / N
k = 1
S = 0

for k in range(1, N + 1):
    S += (h/2) * (sin(a + (k - 1) * h) + sin(a + k * h))
print("台形の面積は" + str(S))