def iterative_prime(number):
    if number < 2:
        return True
    else:
        ans = True
        for i in range(2, round(number**0.5)):
            if number % i == 0:
                ans = False
                break
        return ans




def sieve_prime(number):
    primes = [i for i in range(1, number+1)]
    i = 2
    while i < round(number**0.5) + 1:
        if i in primes:
            for j in range(i*2, number+1, i):
                if j in primes:
                    primes.remove(j)

        i += 1
    return primes

print(iterative_prime(5))
print(sieve_prime(23))
