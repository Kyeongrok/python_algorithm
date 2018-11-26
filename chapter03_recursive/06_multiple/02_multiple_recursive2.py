is_odds = lambda x : x % 2 == 1

def multiply1(n, a):
    if(n == 1): return a

    if (is_odds(n)):
        return multiply1(n // 2, a + a) + a
    else:
        return multiply1(n // 2, a + a)

print(multiply1(4, 5))
print(multiply1(4, 6))