# bronzeIII_10695
import sys
input = sys.stdin.readline

move = [[1,2], [1,-2], [-1,2], [-1,-2],
        [2,1], [2,-1], [-2,1], [-2,-1]]

t = int(input())
for case in range(1, t+1):
    n, r1, c1, r2, c2 = map(int, input().split())
    
    judge = 'NO'
    for x in move:
        r = r1 + x[0]
        c = c1 + x[1]
        if (1<=r<=n and 1<=c<=n) and (r == r2 and c == c2):
            judge = 'YES'
            break
    print(f'Case {case}: {judge}')