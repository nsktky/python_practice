# 以下のルールを持つ再帰関数を実行。
# ・再帰終了条件を持つ
# ・条件を変えながら再帰終了条件に進む
# ・再帰関数は再帰的に関数自身を呼び出す

def bottles_of_beer(bob):

    if bob < 1:
        print('''No more bottles of beer on the wall.
              No more bottles of beer.''')
        return

    tmp = bob
    bob -= 1
    print('''{} bottles of beer on the wall.
          {} bottles of beer.
          Take one down, pass it around.
          {} bottles of beer on the wall.
          '''.format(tmp, tmp, bob))
    bottles_of_beer(bob)

bottles_of_beer(10)