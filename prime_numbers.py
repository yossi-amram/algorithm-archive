#  returns the n-th prime number
def prime(n):
    primes = [2, 3, 5, 7, 11, 13]
    l = 6
    i = 14
    while l < n:
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
            l += 1

        i += 1
    return primes[n - 1]


print(prime(10001))
