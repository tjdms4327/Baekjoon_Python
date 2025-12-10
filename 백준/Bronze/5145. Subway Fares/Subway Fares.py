import sys
input = sys.stdin.readline

k = int(input())
for case in range(1, k+1):
    n = int(input())
    fee = [int(input()) for _ in range(n-1)]
    name = [input().strip() for _ in range(n)]
    
    start = input().strip()
    start_idx = name.index(start)
    end = input().strip()
    end_idx = name.index(end)
    
    distance = abs(end_idx - start_idx)
    print(f'Data Set {case}:')
    print(fee[distance-1])
    print()