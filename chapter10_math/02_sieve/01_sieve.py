from datetime import datetime
def sieve(number):
    prime = [True for number in range(0, number + 1)]
    p = 2
    while(p * p <= number):
        if prime[p] == True:
            for i in range(p*2, number+1, p):
                prime[i] = False
        p = p + 1

    for p in range(0, number):
        if prime[p]:
            print(p)
start = datetime.now()
sieve(100000000)
print(datetime.now() - start)
