# Using recursion

def bigmod(base, power, mod): # base and power is given and we will not calculate the power 
    if power == 0:
        return 1
    elif power % 2 == 1:
        part_1 = base%mod
        part_2 = bigmod(base, power-1, mod)
        return (part_1 * part_2) % mod
    else:
        part_1 = bigmod(base, power // 2, mod)
        return (part_1 * part_1) % mod


ans = bigmod(3, 35, 17)
print(ans)
