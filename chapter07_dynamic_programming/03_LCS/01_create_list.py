
sequence1 = "ABCDCBA"
sequence2 = "DCABDC"

# sequence1 * sequence2만큼의 list만들기

memo = [[0]*len(sequence1)]*len(sequence2)
print(memo)