def is_prime(n):
    for i in range(2, n): # n까지 하면 n-1까지 반복 됨
        print(n, '%', i, '=', n % i)

is_prime(11)