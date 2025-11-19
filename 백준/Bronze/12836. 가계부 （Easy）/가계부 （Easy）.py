# bronzeII_12836
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
days = [0] * (n+1)
for _ in range(q):
    action, p, a = map(int, input().split())
    
    if action == 1:
        days[p] += a
    else:
        print(sum(days[p:a+1]))