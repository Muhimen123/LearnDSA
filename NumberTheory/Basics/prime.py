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
    rn = round(number ** 0.5)
    prime_bool = [True] * (number + 1)
    prime_bool[0] = False
    prime_bool[1] = False
    i = 2
    while i < rn + 1:
        if prime_bool[i] == True:
            for j in range(i*2, number+1, i):
                prime_bool[j] = False

        i += 1

    # Driver code
    primes = []
    for i in range(1, len(prime_bool)):
        if prime_bool[i]:
            primes.append(i)
        else:
            pass

    return primes



print(iterative_prime(5))
print(sieve_prime(10**6))
