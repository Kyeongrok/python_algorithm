# odd홀수 even짝수
def is_odds(number):
    return number % 2 == 1

print(is_odds(10))
print(is_odds(11))

is_odds_lam = lambda x : True if x % 2 == 1 else False

print(is_odds_lam(10))
print(is_odds_lam(11))
