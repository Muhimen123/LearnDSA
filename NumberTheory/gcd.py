def iterative_gcd(num1, num2):
    if num1 == num2 and num1 == 0:
        return None
    elif min(num1, num2) == 0:
        return max(num1, num2)
    else:
        for i in range(2, min(num1, num2) + 1):
            if num1 % i == 0 and num2 % i == 0:
                return i
        return 1


def basic_euclid(num1, num2):
    if num1 == num2 and num1 == 0:
        return None
    elif min(num1, num2) == 0:
        return max(num1, num2)
    else:
        while True:
            if num1 == num2:
                return num1
            else:
                diff = abs(num1 - num2)
                if num1 > num2:
                    num1 = diff
                else:
                    num2 = diff


def improved_euclid(num1, num2):
    if num1 == num2 and num1 == 0:
        return num1
    elif min(num1, num2) == 0:
        return max(num1, num2)
    else:
        while True:
            if num1 == 0:
                return num2
            elif num2 == 0:
                return num1
            else:
                remainder = max(num1, num2) % min(num1, num2)
                if num1 > num2:
                    num1 = remainder
                else:
                    num2 = remainder

print(iterative_gcd(59353,137572))
print(basic_euclid(59353,137572))
print(improved_euclid(59353,137572))
