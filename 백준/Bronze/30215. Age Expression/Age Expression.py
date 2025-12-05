import sys
input = sys.stdin.readline

o, A, K = map(int, input().split())

for a in range(1, o+1):
    k = (o - a*A) % K
    if k == 0 and (o-a*A)>=K:
        print(1)
        sys.exit()
print(0)