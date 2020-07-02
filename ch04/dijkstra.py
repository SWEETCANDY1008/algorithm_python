void Dijkstra(int n, const number W[][], set_of_edges& F) {
   index i, vnear;
   edge e;
   index touch[2..n];
   number length[2..n];

   F = ∅;
   for(i=2;i<=n;i++) {
      touch[i] = 1;
      length[i] = W[1][i];
   }

   repeat(n-1번) {
      min = ∞;
      for(i=2;i<=n;i++) {
         if(0 <= length[i] < min) {
            min = length[i];
            vnear = I;
         }
      e = touch[vnear]가 인덱스인 마디에서
            vnear가 인덱스인 마디로 가는 이음선;
      e를 F에 추가;
      for(i=2;i<=n;i++) {         if(length[vnear] + W[vnear][i] < length[i]) {
            length[i] = length[vnear] + W[vnear][i];
            touch[i] = vnear;
         }
      length[vnear] = -1;
   }
}
