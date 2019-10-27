def solution(seq1, seq2):
    lenSeq1 = len(seq1)
    lenSeq2 = len(seq2)
    dp = [[0] * lenSeq1 for j in range(lenSeq2)]

    # 첫번째 칸
    if(seq2[0] == seq1[0]):
        dp[0][0] == 1

    # 첫번째 줄
    for j in range(lenSeq1):
        if(seq2[0] == seq1[j] and j > 0):
            dp[0][j] = max(dp[0][j - 1], 1)
        else:
            dp[0][j] = max(dp[0][j - 1], 0)

    print(dp)
    print(len(dp))

seq1 = "ABCDCBA"
seq2 = "DCABDC"
solution(seq1, seq2)