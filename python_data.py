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
