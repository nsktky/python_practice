# ITP1_6_B:   Finding Missing Cards

card_list = [[0 for i in range(13)] for j in range(4)]
mark_list = ['S', 'H', 'C', 'D']

n = int(input())
for i in range(n):
    mark, rank = input().split()
    rank = int(rank) - 1
    card_list[(mark_list.index(mark))][rank] = 1

for i in range(4):
    for j in range(13):
        if card_list[i][j] == 0:
            print(mark_list[i], j + 1)