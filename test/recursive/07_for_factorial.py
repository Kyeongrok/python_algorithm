

# recursive function
def recursive_01(n):
    if n == 1:
        return n
    else:
        return n * recursive_01(n - 1)

print(recursive_01(10))

