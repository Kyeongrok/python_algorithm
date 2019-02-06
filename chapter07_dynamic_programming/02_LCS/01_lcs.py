def lcs(string1, string2):
    for i in range(len(string1)):
        for j in range(len(string2)):
            a = string1[i]
            b = string2[j]
            print(i, j, a, b)

    return 0

string1 = "abcdcba"
string2 = "dcabdc"

lcs(string1, string2)

