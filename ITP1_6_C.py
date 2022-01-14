# ITP1_6_C:   Official House

room_list = [[[0 for room in range(10)] for floor in range(3)] for house in range(4)]

n = int(input())
for i in range(n):
    b, f, r, v = map(int, input().split())
    room_list[b - 1][f - 1][r - 1] += v

for house in range(4):
    for floor in range(3):
        for room in range(10):
            print('', room_list[house][floor][room], end='')
        print()
    if house < 3:
        print('####################')