# int bin(int n, int k) {   if(k==0 || n==k)      return 1;
#    else
#       return bin(n-1, k-1) + bin(n-1, k);
# }
   
# int bin2(int n, int k) {
#    index i, j;
#    int B[0..n] [0..k];
   
#    for(i=0;i<=n;i++)
#       for(j=0;j<=minimum(i, k);j++)
#          if(j==0 || j==i)
#             B[i][j] = 1;
#          else
#             B[i][j] = B[i-1][j-1] + B[i-1][j];
#    return B[n][k];}

def minimum(i, k):
    if i > k:
        return k
    elif i < k:
        return i
   
def bin(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return bin(n-1, k-1) + bin(n-1, k)


def bin2(n, k):
    B = []

    for i in range(0, n+1):
        B.insert(i, [1])
        q = minimum(i, k)
        for j in range(0, q+1):
            if j == 0 or j == i:
                B[i].insert(j, 1)
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]
                return B[n][k]

print(bin2(4, 3))