# void prim(int n, const number W[][], set_of_edges& F) {
#    index i, vnear;
#    number min;
#    edge e;
#    index nearest[2..n];
#    number distance[2..n];

#    F = ∅;
#    for(i=2;i<=n;i++) {      nearest[i] = 1;
#       distance[i] = W[1][i];
#    }
#    repeat(n-1 times) {      min = ∞;
#       for(i=2;i<=n;i++)         if(0 <= distance[i] < min) {
#             min = distance[i];
#             vnear = i;
#          }
#       e = vnear가 인덱스인 마디를 Y에 추가한다.
#       add e to F
#       distance[vnear] = -1;
#       for(i=2;i<=n;i++)
#          if(W[i][vnear] < distance[i]) {
#             distance[i] = W[i][vnear];
#             nearest[i] = vnear
#          }
#    }
# }

W = [[0, 1, 3, 999, 999],
     [1, 0, 3, 6, 999],
     [3, 3, 0, 4, 2],
     [999, 6, 4, 0, 5],
     [999, 999, 2, 5, 0]]
n = 5

def prim(n, W):
    # index i, vnear;
    # number min;
    # edge e;
    # index nearest[2..n];
    # number distance[2..n];

    nearest = [999]
    distance = [999]
    F = []

    for i in range(1, n):
        nearest.insert(i, 1)
        distance.insert(i, W[1][i])

    for k in range(1, n-1):
        min = 999
        for i in range(1, n):
            min = distance[i]
            vnear = i
        e 

    repeat(n-1 times) {
        min = ∞;
        for(i=1;i<=n;i++)
        if(0 <= distance[i] < min) {
            min = distance[i];
            vnear = i;
        }
        e = vnear가 인덱스인 마디를 Y에 추가한다.
        add e to F
        distance[vnear] = -1;
        for(i=1;i<=n;i++)
            if(W[i][vnear] < distance[i]) {
            distance[i] = W[i][vnear];
            nearest[i] = vnear



