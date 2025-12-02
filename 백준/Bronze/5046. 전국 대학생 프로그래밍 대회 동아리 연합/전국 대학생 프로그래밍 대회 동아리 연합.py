import sys
input = sys.stdin.readline

n, b, h, w = map(int, input().split())

min_cost = float('inf')
for _ in range(h):
    p = int(input())
    possible = map(int, input().split())
    
    for poss in possible:
        if poss >= n:
            min_cost = min(min_cost, p*n)

if b >= min_cost:
    print(min_cost)
else:
    print('stay home')