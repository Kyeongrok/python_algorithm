def lcs(string1, string2):
    memoList = [[] for _ in range(len(string2))]
    for i in range(len(string1)):
        memoList[j] = [0 for _ in range(len(string1))]
        for j in range(len(string2)):
            print(memoList)
            a = string1[i]
            b = string2[j]

            if a == b:
                print("hello")
            print(i, j, a, b)

    return 0

string1 = "abcdcba"
string2 = "dcabdc"

lcs(string1, string2)

