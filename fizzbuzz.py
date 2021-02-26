# 1~100の数字を出力.
# 3の倍数の時はFizzと表示,3の倍数の時はBuzz,3と5の倍数の時はFizzBuzzと出力

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FIzzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)