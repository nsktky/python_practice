# 入力された文字列が回文になっているか判定
# 回文であればtrue,回文でなければFalseを返す

def palindrome(word):
    # 入力文字の内、大文字を全て小文字に変換
    word = word.lower()
    # wordを[::-1]でスライスすることで文字列を逆順に変換
    return word == word[::-1]

print(palindrome('Mom'))
print(palindrome('Mother'))
print(palindrome('にくのおおいおおのくに'))
