import math


def phi(n):
    ans = []
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            ans.append(i)
    print(len(ans))

def optphi(n):
    ans = [i for i in range(n+1)]
    ln = len(ans)
    for i in range(2, int(ln**0.5)+1):
        if n % i == 0:
            for j in range(i, ln, i):
                if j in ans:
                    ans.remove(j)
    ans.remove(0)
    print(len(ans))

def multiplephi(n):
    # Returns the phi of a number upto the range of n
    ans = [i for i in range(n+1)]
    ln = len(ans)
    for i in range(2, int(ln**0.5) + 1):
        if ans[i] == i:
            prime = ans[i]
            for j in range(i, len(ans), i):
                ans[j] = (prime - 1) * (ans[j]//prime)

    ans.remove(0)
    for i in range(len(ans)):
        print(f"Phi of {i+1} is {ans[i]}")

phi(400)
optphi(400)
multiplephi(400)
