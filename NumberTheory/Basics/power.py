# Program to calculate power

def power(base, expo):
    if base == 0:
        return 0
    elif expo == 0:
        return 1
    elif expo % 2 == 0:
        num_1 = power(base, expo // 2)
        return num_1 * num_1
    else:
        num_1 = base
        num_2 = power(base, expo - 1)
        return num_1 * num_2

base = input("Enter the base: ")
expo = input("Enter the power: ")

print(power(int(base), int(expo)))
