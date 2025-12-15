import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
    n = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    
    max_d = 0
    for i in range(n):
        for j in range(i, n):
            if X[i] == Y[j]:
                d = j-i
                max_d = max(max_d, d)
    
    print(f'The maximum distance is {max_d}')
    if i != t:
        print()