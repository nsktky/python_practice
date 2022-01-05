# ITP1_4_A:   A / B Problem
a, b = map(int, input().split())
d = int(a / b)
r = a % b
f = float(a / b)

print(d, r, format(f, '.10f'))