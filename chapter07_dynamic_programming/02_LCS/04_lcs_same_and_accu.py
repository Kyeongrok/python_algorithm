def lcs(string1, string2):
    memoList = [[] for _ in range(len(string2))]
    for i in range(len(string2)):
        memoList[i] = [0 for _ in range(len(string1))]
        for j in range(len(string1)):
            print(memoList)
            # 같으면 쌓는다.
            if string2[i] == string1[j]:
                memoList[i][j] = memoList[i-1][j-1] + 1
    return 0

string1 = "abcdcba"
string2 = "dcabdc"

lcs(string1, string2)

