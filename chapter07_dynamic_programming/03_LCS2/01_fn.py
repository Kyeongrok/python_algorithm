def solution(seq1, seq2):
    lenSeq1 = len(seq1)
    lenSeq2 = len(seq2)
    dp = [[0] * lenSeq1 for j in range(lenSeq2)]
    print(dp)
    print(len(dp))


seq1 = "ABCDCBA"
seq2 = "DCABDC"
solution(seq1, seq2)