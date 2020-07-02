int minmult(int n, const int d[], index P[][]) {
   index i, j, k, diagonal;
   int M[1..n][1..n];

   for(i=1;i<=n;i++)
      M[i][i] = 0;
   for(diagonal = 1 ;diagonal<=n-1;diagonal++)
      for(i=1;i<=n-diagonal;i++) {
         j=i+diagonal
         M[i][j] = min┬(𝑖≤𝑘≤𝑗−1)⁡〖(𝑀[𝑖][𝑘]+𝑀[𝑘+1][𝑗]+𝑑[𝑖−1]∗𝑑[𝑘]∗𝑑[𝑗]);〗
         P[i][j] = 최소 횟수를 나타내는 k의 값;
      }
   return M[1][n];
}
      
void order(index i, index j) {
   if(i==j)
      cout << “A” << I
   else {
      k = P[i][j];
      cout << “(“;
      order(i, k);
      order(k+1, j);
      cout << “)”;
   }
}
