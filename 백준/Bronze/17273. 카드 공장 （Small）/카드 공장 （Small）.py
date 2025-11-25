import sys
input = sys.stdin.readline

n, m = map(int, input().split())
front, back = [], []
for _ in range(n):
    a,b = map(int, input().split())
    front.append(a)
    back.append(b)
    
now = front[:]
for _ in range(m):
    x = int(input())
    for i in range(n):
        if now[i] <= x:
            if front[i] == now[i]:
                now[i] = back[i]
            else:
                now[i] = front[i]
print(sum(now))