seq1 = "ABCDCBA"
seq2 = "DCABDC"

# seq1 * seq2만큼의 list만들기
memo = [ [0] * len(seq1) ] * len(seq2)
print(memo)

