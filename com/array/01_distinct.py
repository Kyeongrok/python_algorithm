arr1 = [
    "a", "b", "c"
]
arr2 = [
    "b", "c", "d", "e"
]

def distinct(arr1, arr2):

    # 두개 합친담에 set으로 바꾼다

    return  list(set(arr1 + arr2))

print(distinct(arr1, arr2))
