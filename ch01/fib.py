def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


print(fib(4))

def fib2(n):
    f = []
    f.insert(0, 0)      # f[0] = 0
    if n > 0:
        f.insert(1, 1)  # f[1] = 1
        for i in range(2, n+1):
            f.insert(i, f[i-1] + f[i-2])  # f[i] = f[i-1] + f[i-2]
    return f[n]

print(fib2(4))