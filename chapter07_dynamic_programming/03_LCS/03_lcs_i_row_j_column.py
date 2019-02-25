def lcs(string1, string2):
    memoList = [[] for _ in range(len(string2))]
    for i in range(len(string2)):
        memoList[i] = [0 for _ in range(len(string1))]
        for j in range(len(string1)):
            print(memoList)
    return 0

string1 = "ABCDCBA"
string2 = "DCABDC"

lcs(string1, string2)

