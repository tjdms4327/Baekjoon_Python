import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, 1+t):
    n, p, q = map(int, input().split())
    weight = list(map(int, input().split()))
    weight.sort()
    
    cur = [0,0]
    for w in weight:
        if cur[1]+w<=q and cur[0]+1<=p:
            cur[1] += w
            cur[0] += 1
            
    print(f'Case {case}: {cur[0]}')