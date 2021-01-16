def say_something():
    print('hi')

say_something()
print(type(say_something))


def say_something2():
    s = 'hi'
    return s

result = say_something2()
print(result)


def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this('red')
result2 = what_is_this('green')
result3 = what_is_this('orange')
print(result)
print(result2)
print(result3)


def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

# 引数を指定しないと想定している変数に入らない
menu('beef', 'ice', 'beer')
# キーワードを指定
menu(entree='beef', dessert='ice', drink='beer')
# キーワード引数と位置引数は両立できるが、場所に注意が必要
menu('beef', dessert='ice', drink='beer')

print('#####################################')
def dinner_menu(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

dinner_menu('fish', drink='beer')


# 引数に空のリスト渡さないほうがいい
def test_func(x, l=[]):
    l.append(x)
    return l

r = test_func(100)
print(r)

# 空のリストは参照渡しされているから空のリストに再び100追加ではなく、
# 最初に作られたリストに再度100が追加される
r = test_func(100)
print(r)


# 関数内で初期化してあげれば、いつ値を渡しても空のリストに入れられる
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func(100)
print(r)

r = test_func(100)
print(r)
