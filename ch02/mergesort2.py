def mergesort2(n, S):
    if n > 1:
        h = n // 2
        m = n - h
        U = S.slice(0, h)
        V = S.slice(h+1, n)
        mergesort(h, U)
        mergesort(m, V)
        merge(h, m, U, V, S)

def merge(h, m, U, V, S):
    i = 0
    j = 0
    k = 0
    while i <= h and j <= m:
        if U[i] < V[j]:
            S[k] = U[i]
            i = i + 1
        else:
            S[k] = V[j]
            j = j + 1
        k = k + 1
    if i > h:
        for x in range(k, h+m):
            S[x] = V.slice(j, m)
    else:
        for x in range(k, h+m):
            S[x] = U.slice(i, h)


S = [27, 10, 12, 20, 25, 13, 15, 22]

print(mergesort(8, S));

void mergesort2(index low, index high) {
   index mid;
   if(low<high) {
      mid=(low+high)/2
      mergesort2(low, mid);
      mergesort2(mid+1, high);
      merge2(low, mid, high);
   }
}


void merge2(index low, index mid, index high) {
   index i, j, k
   keytype U[low..high]
   i=low; j=mid+1; k=low;
   while(i<=mid && j<=high) {
      if(S[i] < S[j]) {         U[k] = S[i];
         i++;
      } else {
         U[k] = S[j];
         j++;
      }
      k++;
   }
   if(i>mid)
      move S[j] through S[high] to U[k] through U[high];
   else
      move S[i] through S[mid] to U[k] through U[high]; 
   move U[low] through U[high] to S[low] through S[high];
}
