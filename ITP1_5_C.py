# ITP1_5_C:   Print a Chessboard
while True:
    H, W = map(int, input().split())

    if H == 0 and W == 0:
        break

    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if (i % 2) != 0 and (j % 2) !=0:
                print('#', end='')
            elif (i % 2) == 0 and (j % 2) !=0:
                print('.', end='')
            elif (i % 2) != 0 and (j % 2) ==0:
                print('.', end='')
            else:
                print('#', end='')
        print()
    print()