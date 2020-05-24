import random


def recur_gcd(num1, num2, i):
    # Not suitabe for big numbers
    if num1 % i == num2 % i and num1 % i == 0:
        j = i
        print(i)
        return None
    else:
        recur_gcd(num1, num2, i - 1)

def recur_euclid(num1, num2):
    # Not suitable for big numbers
    if num1 == num2:
        print(num1)
        return num1
    else:
        diff = abs(num1 - num2)
        if num1 > num2:
            num1 = diff
        else:
            num2 = diff

        recur_euclid(num1, num2)

def recur_adv_euclid(num1, num2):
    # Suitale for all numbers
    if num1 == 0:
        print(num2)
        return num2
    elif num2 == 0:
        print(num1)
        return num1
    else:
        remainder = max(num1, num2) % min(num1, num2)
        if num1 > num2:
            num1 = remainder
        else:
            num2 = remainder
        recur_adv_euclid(num1, num2)


num1 = random.randint(50, 50000000000000)
num2 = random.randint(50, 50000000000000)
print(num1, num2)
recur_euclid(num1, num2)
recur_adv_euclid(num1, num2)
