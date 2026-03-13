import sys
input = sys.stdin.readline
from collections import deque

m, s = map(int, input().split(':'))
target = m*60 + s


queue = deque([(0,0,0)])  # time, cooking, button_count
visited = [[False]*2 for _ in range(3601)]
visited[0][0] = True

while queue:
    time, cooking, cnt = queue.popleft()
    if time == target and cooking == 1:
        print(cnt)
        break
    
    for nt in [time+10, time+60, time+600]:
        if nt <= 3600 and not visited[nt][cooking]:
            visited[nt][cooking] = True
            queue.append((nt, cooking, cnt+1))

    # 조리시작
    if cooking == 0:
        nt = 30 if time == 0 else time
        if nt <= 3600 and not visited[nt][1]:
            visited[nt][1] = True
            queue.append((nt, 1, cnt+1))
    else:
        nt = time + 30
        if nt <= 3600 and not visited[nt][1]:
            visited[nt][1] = True
            queue.append((nt, 1, cnt+1))