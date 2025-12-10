import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    k, *X = map(int, input().split())
    
    ok = True
    for i in range(k):
        if i in [0,1]:
            continue
        elif X[i-2]+X[i-1] == X[i]:
            continue
        else:
            print('NO')
            ok = False
            break
    if ok:
        print('YES')