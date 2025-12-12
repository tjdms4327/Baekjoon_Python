import sys
input = sys.stdin.readline

k = int(input())
for case in range(1, 1+k):
    n, v = map(int, input().split())
    ad = [tuple(map(int, input().split())) for _ in range(n)]
    
    tot = 0
    for _ in range(v):
        a1, a2, c = map(int, input().split())
        d1, p1 = ad[a1-1]
        d2, p2 = ad[a2-1]
        
        if d1 == 1:
            tot += p1
        if d2 == 1:
            tot += p2
            
        if c == 1:
            if d1 == 0:
                tot += p1
        elif c == 2:
            if d2 == 0:
                tot += p2
    
    print(f'Data Set {case}:\n{tot}\n')  