# stackのデータ構造を構築

class Stack:
    def __init__(self):
        self.items = []

# stackが空か判定
    def is_empty(self):
        return self.items == []

# stackに要素を追加
    def push(self, item):
        return self.items.append(item)

# stackの最後に追加された要素を削除
    def pop(self):
        return self.items.pop()

# stackの最後の要素を表示
    def peek(self):
        last = len(self.items) - 1
        if last >= 0:
            return self.items[last]
        else:
            return None

# stackに格納されたデータ数を表示
    def size(self):
        return len(self.items)


stack = Stack()
print(stack.is_empty())

stack.push(1)
print(stack.is_empty())
print(stack.peek())

stack.pop()
print(stack.is_empty())
print(stack.peek())

for i in range(0, 6):
    stack.push(i)

print(stack.peek())
print(stack.size())
stack.pop()
print(stack.peek())
print(stack.size())

# stackを用いて文字列を逆順にする
stack2 = Stack()

text = 'hello'

for c in text:
    stack2.push(c)

reverse = ''

while stack2.size():
    reverse += str(stack2.pop())

print(reverse)