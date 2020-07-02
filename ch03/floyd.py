n = 5
W = [[0, 1, 999, 1, 5],
     [9, 0, 3, 2, 999],
     [999, 999, 0, 4, 999],
     [999, 999, 2, 0, 3],
     [3, 999, 999, 999, 0]
    ]

def minimum(x, y):
    if x < y:
        return x
    elif x > y:
        return y
    else:
        return x

def floyd(n, W):
    D = W

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                D[i][j] = minimum(D[i][j], D[i][k]+D[k][j])
    return D

print(floyd(n, W))

#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#

n = 5
W = [[0, 1, 999, 1, 5],
     [9, 0, 3, 2, 999],
     [999, 999, 0, 4, 999],
     [999, 999, 2, 0, 3],
     [3, 999, 999, 999, 0]
    ]

def floyd2(n, W):
    P = []
    for i in range(0, n):
        P.insert(i, [])
        for j in range(0, n):
            P[i].insert(j, 0)
    D = W

    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if D[i][k] + D[k][j] < D[i][j]:
                    P[i][j] = k
                    D[i][j] = D[i][k]+D[k][j]

    return P


P = floyd2(n, W)
print(P)

def path(q, r):
    if P[q][r] != 0:
        path(q, P[q][r])
        print("v" + str(P[q][r]))
        path(P[q][r], r)

path(4, 2)          # 배열이기 때문에 인덱스가 0부터 시작이므로 실제 정점에서는 5에서 3
