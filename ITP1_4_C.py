# ITP1_4_C:   Simple Calculator

while True:
    a, op, b = input().split()
    a = int(a)
    b = int(b)

    if op == '?':
        break
    elif op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(int(a / b))
