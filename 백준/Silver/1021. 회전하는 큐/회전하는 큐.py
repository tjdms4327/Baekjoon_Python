import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
queue = deque([*range(1, n+1)])

targets = list(map(int, input().split()))

cnt = 0
for x in targets:
    idx = queue.index(x)
    
    if idx <= len(queue)//2:
        cnt += idx
        queue.rotate(-idx) # 왼쪽으로 이동
    else:
        cnt += len(queue) - idx
        queue.rotate(len(queue) - idx)
    queue.popleft()
    
print(cnt)