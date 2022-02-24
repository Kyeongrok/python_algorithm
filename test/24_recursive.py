arr = [7, 3, 2, 9]

def sum(arr, r):
    if len(arr) > 0:
        return sum(arr, r + arr.pop())
    else:
        return r

print(sum(arr, 0))

seq1 = ['A', 'B', 'C', 'D', 'C', 'B', 'A']
seq2 = ['D', 'C', 'A', 'B', 'D', 'C']