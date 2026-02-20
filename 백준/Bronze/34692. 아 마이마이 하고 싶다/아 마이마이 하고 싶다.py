import sys
input = sys.stdin.readline
import heapq

n, m, k = map(int, input().split())
T = list(map(int, input().split()))

heap = [0]*m
for t in T:
    x = heapq.heappop(heap)
    heapq.heappush(heap, x+t)

a = heapq.heappop(heap)
if a > k:
    print('GO')
else:
    print('WAIT')