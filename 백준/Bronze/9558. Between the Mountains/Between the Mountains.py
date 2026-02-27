import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    _, *A = list(map(int, input().split()))
    _, *B = list(map(int, input().split()))
    
    Min = float('inf')
    for a in A:
        for b in B:
            Min = min(Min, abs(a-b))
    print(Min)