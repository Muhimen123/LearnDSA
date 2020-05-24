import math

def with_gcd(num1, num2):
    ans = (num1 * num2) // math.gcd(num1, num2)
    return ans

def without_gcd(num1, num2):
    small = min(num1, num2)
    big = max(num1, num2)
    inc = big
    while True:
        if big % small == 0:
            return big
        else:
            big += inc

print(with_gcd(8,5))
print(without_gcd(8,5))
