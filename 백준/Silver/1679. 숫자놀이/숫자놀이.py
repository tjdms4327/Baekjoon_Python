import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
nums = list(map(int, input().split()))
k = int(input())

max_sum = max(nums) * k
reachable = [False] * (max_sum + 1) # 결과 저장

queue = deque([(0,0)])   # (sum, count)
visited = [[False]*(k+1) for _ in range(max_sum+1)]
visited[0][0] = True

while queue:
    s, cnt = queue.popleft()
    
    if s > 0:
        reachable[s] = True
        
    if cnt == k:
        continue
    
    for x in nums:
        ns = s + x
        nc = cnt + 1
        
        if ns <= max_sum and not visited[ns][nc]:
            visited[ns][nc] = True
            queue.append((ns, nc))

for i in range(1, max_sum+1):
    if not reachable[i]:
        if i % 2:
            print(f"jjaksoon win at {i}")
        else:
            print(f"holsoon win at {i}")
        break