seq1 = "ABCDCBA"
seq2 = "DCABDC"
memo = [[0]*len(seq1)]*len(seq2)

# seq1, seq2에서 문자열 한개씩 뽑기
for i in range(len(seq2)):
    for j in range(len(seq1)):
        print("({}, {}) = ({}, {})".format(i, j, seq2[i], seq1[j]) )
