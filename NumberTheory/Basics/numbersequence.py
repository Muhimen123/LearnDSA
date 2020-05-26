class fib:
    def iterative_fib(self, n): # Returns the fibonacci sequence upto n
        ls = [0] * n
        ls[0] = 0
        ls[1] = 1
        ls[2] = 1
        for i in range(3, n):
            ls[i] = ls[i-1] + ls[i-2]
        print(ls)

    def ith_num(self, n):
        # Prints the ith fib number
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.ith_num(n-1) + self.ith_num(n-2)

seq = fib()
seq.iterative_fib(15)
print(seq.ith_num(9))
