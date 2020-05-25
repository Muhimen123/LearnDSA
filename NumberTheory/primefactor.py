def factor(n):
    m = n
    while n % 2 == 0:
        print(2, end=" ")
        n /= 2
    i = 3
    while i <= round(m ** 0.5)+1:
        if n % i == 0:
            n /= i
            print(i, end=" ")
        else:
            i += 2
    
    if n > 2:
        print(round(n))
        
def prime_factor_sieve(n):
    ls = [i for i in range(n+1)]
    for i in range(4, len(ls), 2):
        ls[i] = 2
    for i in range(3, round(len(ls)**0.5) + 1):
        if ls[i] == i:
            for j in range(i*i, len(ls), i):
                if ls[j] == j:
                    ls[j] = i

    ans_list = []
    while n != 1:
        ans_list.append(ls[n])
        n = n // ls[n]

    print(*ans_list)

n = int(input("Enter a number here: "))
#factor(n)
prime_factor_sieve(n)
