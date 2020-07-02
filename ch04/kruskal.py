void kruskal(int n, int m, set_of_edges E, set_of_edges& F) {
   index i, j;
   set_pointer p, q;
   edge e;

   E에 속한 m개의 이음선을 가중치가 작은 것부터 차례로 정렬한다.
   F = ∅;
   initial(n);		// n개의 서로소 부분집합을 초기화
   while(n-1개의 이음선 개수만큼) {
      e = 아직 고려하지 않은 이음선 중 가중치가 최소인 이음선
      i, j = e로 연결된 마디의 인덱스
      p = find(i);
      q = find(j);
      if(! equal(p, q)) {
         merge(p, q);
         e를 F에 추가;
      }
   }
}
