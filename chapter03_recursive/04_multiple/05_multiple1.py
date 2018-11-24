is_odds = lambda x : x % 2 == 1

def multiple1(n, a):
    if(n == 1): return a
    result = multiple1(n // 2, a + a)
    if(is_odds(n)): result = result + a
    return result

print(multiple1(4, 5))