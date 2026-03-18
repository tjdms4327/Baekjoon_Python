import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())
one = input().strip()[::-1]
two = input().strip()
t = int(input())

ants = []
for x in one:
    ants.append((x, 1))
for x in two:
    ants.append((x, -1))
    
for _ in range(t):
    i = 0
    while i < n1+n2-1:
        if ants[i][1]==1 and ants[i+1][1]==-1:
            ants[i], ants[i+1] = ants[i+1], ants[i]
            i += 2
        else:
            i += 1

print(''.join(c for c, _ in ants))