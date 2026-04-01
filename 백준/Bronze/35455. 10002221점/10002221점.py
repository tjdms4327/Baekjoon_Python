import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    
    MAX = n + 10**7
    if s == MAX:
        print('Yes')
    else:
        print('No')