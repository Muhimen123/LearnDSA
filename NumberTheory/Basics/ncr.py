from math import gcd

def ncr(n, r):
    p = 1
    k = 1

    r = min(r, n - r)

    if r != 0:
        while r != 0:
            p *= n
            k *= r

            m = gcd(p, k)

            p //= m
            k //= m

            n -= 1
            r -= 1

    else:
        p = 1

    return p


print(ncr(30, 15))
print(ncr(50, 25))
print(ncr(100, 6))
