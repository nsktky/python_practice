# 入力された2値がアナグラムの関係か判定する

def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    # sortedで文字列をソートし、ソート後の文字列が一致すれば回文と判定しtrueを返す
    return sorted(word1) == sorted(word2)

print(anagram('Iceman', 'Cinema'))
print(anagram('mam', 'dad'))
print(anagram('すがわらぶんた', 'ぶたがすわらん'))