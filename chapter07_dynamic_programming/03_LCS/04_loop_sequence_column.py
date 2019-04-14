
sequence1 = "ABCDCBA"
sequence2 = "DCABDC"

# sequence1 * sequence2만큼의 list만들기
memo = [[0]*len(sequence1)]*len(sequence2)

for i in range(len(sequence2)):
    for j in range(len(sequence1)):
        seq2i = sequence2[i]
        seq1j = sequence1[j]
        if(i == 0 and seq2i == seq1j):
            memo[i][j] = 1
print(memo)
