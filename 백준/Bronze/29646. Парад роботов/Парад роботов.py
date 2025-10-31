import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
robots = deque(list(map(float, input().split())) for _ in range(n))

Xsum = sum(x for x, y in robots)
Ysum = sum(y for x, y in robots)
for _ in range(k):
    x_new = Xsum / n
    y_new = Ysum / n
    
    x_front, y_front = robots.popleft()
    Xsum -= x_front
    Ysum -= y_front

    robots.append([x_new, y_new])
    Xsum += x_new
    Ysum += y_new

print(*robots[-1])
