import sys
input = sys.stdin.readline

k = int(input())
for case in range(1, k+1):
    c, b, n, r = map(int, input().split())
    companies = list(map(int, input().split()))
    
    C = [tuple(map(int, input().split())) for _ in range(n)]
    tot = 0
    for ci, pi in C:
        if ci in companies:
            tot += pi*r // 100
    
    print(f'Data Set {case}:')
    print(tot, '\n')