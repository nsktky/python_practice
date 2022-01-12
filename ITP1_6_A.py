# ITP1_6_A:   Reversing Numbers

n = int(input())
num_list = list(map(int, input().split()))

num_list.reverse()

for i in range(n):
    if i < (n - 1):
        print(num_list[i], end=' ')
    else:
        print(num_list[i])