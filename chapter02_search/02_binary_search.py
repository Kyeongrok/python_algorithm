def binary_search(list, what_i_want_to_find):
    low = 0
    high = len(list)

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if(guess == what_i_want_to_find):
            print(mid)
            break
        elif (guess < what_i_want_to_find):
            low = mid + 1
        else:
            high = mid - 1
        print("mid:{}, guess:{}, low:{}".format(mid, guess, low))

list = list(range(0, 1000))
what_i_want_to_find = 80
binary_search(list, what_i_want_to_find)