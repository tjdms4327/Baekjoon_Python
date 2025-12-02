import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, t+1):
    n = int(input())
    H = list(map(int, input().split()))
    
    count = 0
    for i in range(1, n-1):
        if H[i-1] < H[i] and H[i] > H[i+1]:
            count += 1
    print(f'Case #{case}: {count}')