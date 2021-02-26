# 入力された文字列に対し、どの文字が何回使われたかを数える

def count_characyers(word):
    # 辞書に文字と使われた回数を格納し数える
    count_dic = {}
    for c in word:
        if c in count_dic:
            count_dic[c] += 1
        else:
            count_dic[c] = 1

    print(count_dic)

count_characyers('Hello World')

# collections.Counterを使えば一行で実装できる…便利か？先人ありがとうな
from collections import Counter

print(Counter('Hello World 2'))