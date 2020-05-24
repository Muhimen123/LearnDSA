import math

ls = list(map(int, input("Enter the numbers: ").split()))
if len(ls) < 2:
    print("More numbers required")
else:
    for i in range(len(ls)-1):
        gcd  = math.gcd(ls[i], ls[i+1])
        ls[i] = -1
        ls[i+1] = gcd

    print(ls[-1])
