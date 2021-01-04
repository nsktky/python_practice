num = 1
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

num = name
print(num, type(num))

str_num = '1'
new_num = int(str_num)

print(new_num, type(new_num))


# 型宣言も一応できる
num2: int = 2
name2: str ='2'
num2 = name2

print(num2, type(num2))


print('Hi', 'Mike', sep=',', end='')
print('Hi', 'Mike', sep=',')



import math

result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)

# print(help(math))


s = 'test'

print(s)
print('I don\'t know')
print('hello. \nHow are you?')
print(r'C:\name\name')

print('#####################')
print("""\
line1
line2
line3\
""")
print('#####################')

print('Hi' * 3 + 'Mike')
print('py' + 'thon')


word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print(word[:2])
print(word[2:])
print('##########################')
word = 'j' + word[1:]
print(word)
print(word[:])
n = len(word)
print(n)


s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('X')
print(is_start)

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))


a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'takuya'
family = 'nosaka'
print(f'My name is {name} {family}. Watashi ha {family} {name}')