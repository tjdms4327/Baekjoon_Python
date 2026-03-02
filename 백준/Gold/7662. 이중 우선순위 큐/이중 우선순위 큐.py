import sys
input = sys.stdin.readline
import heapq

t = int(input())
for _ in range(t):
    k = int(input()) # 연산 수

    min_heap = []
    max_heap = []
    visited = [False] * k

    for i in range(k):
        command, n = input().strip().split()
        n = int(n)
        
        if command == 'I':
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
            visited[i] = True
            
        elif command == 'D':
            if n == 1:  # 최댓값 삭제
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False # 삭제한 거 표시
                    heapq.heappop(max_heap)
                    
            elif n == -1:  # 최솟값 삭제
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
                    
     # 유효하지 않은 값 제거
    while min_heap and not visited[min_heap[0][1]]: # 삭제 표시한 거 이제 처리
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    if not min_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])