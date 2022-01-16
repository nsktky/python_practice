# ITP1_6_D:   Matrix Vector Multiplication
n, m = map(int, input().split())
A = []
B = []

for i in range(n):
    A.append([int(j) for j in input().split()])

for i in range(m):
    B.append(int(input()))

for i in range(n):
    answer = 0
    for j in range(m):
        answer += A[i][j] * B[j]
    print(answer)