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

count = 0
while True:
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue

    print(count)
    count += 1


count = 0

# whileでbreakされなければelseにいく
while count < 5:
    print(count)
    count += 1
else:
    print('done')

# 正しいinputがあるまでループする処理
# while True:
#     word = input('Enter:')
#     num = int(word)
#     if num == 100:
#         break
#     print('next')


print('################################')
# for文
some_list = [1, 2, 3, 4, 5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

for i in some_list:
    print(i)

for s in 'abcde':
    print(s)

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        continue
    if word == 'is':
        break
    print(word)

# breakで抜けるとelseに行かない
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all')


print('###########################')
# range関数

# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in num_list:
#     print(i)

for i in range(2, 10, 3):
    print(i)

# _にすることで、for文の中でiなどの変数使わないことを明示
for _ in range(10):
    print('hello')



print('###########################')
# zip関数

days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

# for i in range(len(days)):
#     print(days[i], fruits[i], drinks[i])

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)


print('###########################')
# dicのfor処理

d = {'x': 100, 'y': 200}
print(d.items())

for k, v in d.items():
    print(k, ':', v)