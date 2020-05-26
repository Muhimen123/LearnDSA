def iterative(n): # Iterative version for getting the factorial
    ans = 1
    for i in range(n, 1, -1):
        ans *= i
    return ans


def recursive(n):
    if n == 0:
        return 1
    else:
        return n * recursive(n - 1)
    

print(iterative(10))
print(recursive(10))
