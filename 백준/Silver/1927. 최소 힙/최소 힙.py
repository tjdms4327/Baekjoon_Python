import sys
input = sys.stdin.readline
import heapq

n = int(input())

heap = []
for _ in range(n):
    x = int(input())
    
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    elif x > 0:
        heapq.heappush(heap, x)