# ITP1_5_B:   Print a Frame

while True:
    H, W = map(int, input().split())

    if H == 0 and W == 0:
        break

    for i in range(H):
        for j in range(W):
            if i == 0 or j ==0:
                print('#', end='')
            elif i == (H - 1) or j == (W - 1):
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()