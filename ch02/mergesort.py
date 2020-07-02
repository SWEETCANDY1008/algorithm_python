def mergesort(n, S):
    if n > 2:
        h = n // 2
        m = n - h
        U = []
        V = []
        U = S[0: h]
        V = S[h: n]
        mergesort(h, U)
        mergesort(m, V)
        merge(h, m, U, V, S)

def merge(h, m, U, V, S):
    i = 0
    j = 0
    k = 0
    while i < h and j < m:
        if U[i] < V[j]:
            S[k] = U[i]
            i = i + 1
        else:
            S[k] = V[j]
            j = j + 1
        k = k + 1
    if i > h:
        for x in range(k, h+m):
            S[x] = V[j]
            j = j + 1
    else:
        for x in range(k, h+m):
            S[x] = U[i]
            i = i + 1


S = [27, 10, 12, 20, 25, 13, 15, 22]

mergesort(8, S)
print(S)