import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, 1+t):
    n, w = map(int, input().split())
    samples = list(map(int, input().split()))
    
    result = []
    for i in range(n-w+1):
        result.append(sum(samples[i:i+w]) // w)
    
    print(f'Data Set {case}:')
    print(abs(max(result) - min(result)))
    print()