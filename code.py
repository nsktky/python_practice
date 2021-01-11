# if文

x = -10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('10')
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('positive')
    if b > 0:
        print('b is positive')


# 論理演算子
print('#######################################')

a = 2
b = 1

if a == b:
    print('a=b')

if a != b:
    print('a is not b')

if a < b:
    print('a < b')

if a > b:
    print('a > b')

if a <= b:
    print('a <= b')

if a >= b:
    print('a >= b')

if a > 0 and b > 0:
    print('a and b are positive')

# 以下でも同じだがコードが長くなる
# if a > 0:
#     if b > 0:
#        print('a and b are positive')

if a > 0 or b > 0:
    print('a or b are positive')

# 以下でも同じだがコードが長くなる
# if a > 0:
#     print('a or b are positive')
# elif b > 0:
#     print('a or b are positive')


# inとnot
print('########################################')
y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

if not a == b:
    print('Not equal')

if not a > b:
    print('Not equal')


is_ok = True

if not is_ok:
    print('hello')

# 以下と一緒だが、分かりにくいのでnotがいい
# if is_ok != True:
#     print('hello')


print('###############################')
# 値のない値の判定
# False, 0, 0.0, '', [], (), {}, set() 全てFalseとなる
is_ok = True
is_ok = [1, 2, 3, 4]

# 変数に値が入っていたらokを返す。値の型は問わない
if is_ok:
    print('ok')
else:
    print('no')

# リストに値があるか判定する場合、下記のように要素数が0より大きいとする必要はない
# if len(list) > 0:　これでもいいが…
# if list: これでいい

print('###############################')
# noneの判定
is_empty = None


if is_empty is None:
    print('None!')

# これでもいいが、Noneの判定はisを使う
# if is_empty == None:
#     print('None!')

# 1の値とtrueの値が等しいか判断
print(1 == True)
# 1とtrueが等しいか判断
print(1 is True)


print('###############################')
# while文
count = 0

while count < 5:
    print(count)
    count += 1