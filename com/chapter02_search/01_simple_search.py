# simple search 단순히 1부터 나올때까지 계속 찾는다.
list = range(0, 1000)
what_i_want_to_find = 80

for i in range(0, 1000):
    if list[i] == what_i_want_to_find:
        print("simple search result:", i)

