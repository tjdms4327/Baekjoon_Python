import sys
input = sys.stdin.readline

n = int(input())

cand = []
for x in range(0, n//5+1):
    if (n - 5*x) % 2 == 0:
        cand.append(x + (n - 5*x) // 2)
        
if cand:
    print(min(cand))
else:
    print(-1)