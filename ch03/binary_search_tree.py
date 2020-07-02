void search(node_pointer tree, keytype keyin, node_pointer& p) {
   bool found;

   p = tree;
   found = false;
   while(!found)
      if(p->key == keyin)
         found = true;
      else if(keyin < p->key);
         p = p->left;
      else
         p = p->right
}

void optsearchtree(int n, const float p[], float& minavg, index R[][]) {
   index i, j, k, diagonal;
   float A[1..n+1][0..n];
   for(i=1;i<=n;i++) {
      A[i][i-1] = 0;
      A[i][i] = p[i];
      R[i][i] = I;
      R[i][i-1] = 0;
   }
   A[n+1][n] = 0;
   R[n+1][n] = 0;
   for(diagonal = 1;diagonal<=n-1;diagonal++)
      for(i=1;i<=n-diagonal;i++) {         j = I + diagonal;
         A[i][j] = min┬(𝑖≤𝑘≤𝑗−1)⁡(𝐴[𝑖][𝑘−1]+𝐴[𝑘+1][𝑗])+ ∑_(𝑚=𝑖)^𝑗▒𝑝_𝑚 
         R[i][j] = 최소값을 주는 k의 값;
      }
   minavg = A[1][n];
}

node_pointer tree(index I, j) {
   index k;
   node_pointer p;
   
   k = R[i][j]
   if(k == 0)
      return NULL;
   else {
      p = new_nodetype;
      p->key = Key[k];
      p->left = tree(I, k-1);
      p->right = tree(k+1, j);
      return p;
   }
}

