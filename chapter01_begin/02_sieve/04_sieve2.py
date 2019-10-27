def sieve(number):
    prime = [True for number in range(number + 1)]
    p = 2
    while(p * p <= number):
        if prime[p] == True:
            for i in range(p*2, number+1, p):
                prime[i] = False
        p = p + 1

    for p in range(2, number):
        if prime[p]:
            print(p)

sieve(100)
