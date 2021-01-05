r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))

print(r.count(3))

if 5 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)


# 値渡しと参照渡し リストや辞書型は参照渡しになる。コピーする際は注意が必要
i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('J = ', j)
print('J = ', i)

x = [1, 2, 3, 4, 5]
y = x.copy()
# y = x[:]
y[0] = 100
print('y =', y)
print('y =', x)

X = 20
Y = X
Y = 5
print(id(X))
print(id(Y))
print(Y)
print(X)

X = ['a', 'b']
Y = X
Y[0] = 'p'
print(id(X))
print(id(Y))
print(Y)
print(X)


###tuple

num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = 10, 20
print(x, y)

min, max = 0, 100
print(min, max)

# a, b, c, d, e, f = 'Mike', '1', '1', '1', 'e', 'f'
# 長くなると読みにくいからだめ
a = 'Mike'
b = '1'

# アンパッキング
i = 10
j = 20
tmp = i
i = j
j = tmp

print(i, j)

a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)


# tupleは変更できないので、変えたくないものを入れておくのに良い。
# あとで間違えてもエラーが出るのでバグとわかる。

chose_from_two = ('A', 'B', 'C')
# chose_from_two = ['A', 'B', 'C']

answer = []

# chose_from_two.append('A')
# chose_from_two.append('C')

answer.append('A')
answer.append('B')

print(chose_from_two)
print(answer)

# 辞書型の参照渡し

x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

# 辞書型はハッシュテーブルを用いている。
# キーがわかればすぐvalueを取り出せる。リストで実装もできるけど、普通は辞書型
fruits ={
    'apple': 100,
    'banana': 200,
    'orange': 300,
}

print(fruits['apple'])


# 集合
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
# 共通の友達を表示
print(my_friends & A_friends)

# リストに追加されたものの種類だけを表示
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)