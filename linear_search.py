# リストの中に該当の数があるか調べる
# リストの最初から順番に突合し、一致する数があればtrue,なければfalseを返す（線形探索）

def liner_search(num_list, num):
    found = False
    for i in num_list:
        if i == num:
            found = True
            break
    return found

numbers = range(0, 100)
result1 = liner_search(numbers, 55)
print(result1)

result2 = liner_search(numbers, 1000000)
print(result2)
