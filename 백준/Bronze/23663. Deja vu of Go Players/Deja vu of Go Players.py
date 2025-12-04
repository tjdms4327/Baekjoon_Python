import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    Red = list(map(int, input().split()))
    White = list(map(int, input().split()))
    
    if n <= m:
        print('Yes')
    else:
        print('No')