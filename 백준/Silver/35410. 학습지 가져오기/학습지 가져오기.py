import sys, heapq
input = sys.stdin.readline

n = int(input())
T = list(map(int, input().split()))
T.sort()

heap = []
now = 0
i = 0
while i<n or heap:
    while i<n and T[i]<=now:
        heapq.heappush(heap, -T[i])
        i += 1
        
    if not heap:
        now = T[i]
        continue

    heapq.heappop(heap)
    now += 1

print(now)    