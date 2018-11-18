# 196, 42
def gcd(first, second):
    # gcd(196, 42) = gcd(196 - 42, 42)
    # gcd(154, 42) = gcd(154 - 42, 42)
    # gcd(112, 42) = gcd(112 - 42, 42)
    # gcd(70, 42) = gcd(70 - 42, 42)
    # gcd(28, 42) = gcd(28, 42 - 28)
    # gcd(28, 14) = gcd(28 - 14, 14)
    # gcd(14, 14)

    return 1

print(gcd(196, 42))