import math


def coef(a, b):
    ls = [i for i in range(a, a-b, -1)]
    ls2 = [i for i in range(1, b+1)]
    ans = math.prod(ls) // math.prod(ls2)
    print(ans)

a, b = map(int, input("Enter two numbers: ").split())
coef(a, b)
