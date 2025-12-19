import sys
input = sys.stdin.readline

k = int(input())
for _ in range(k):
    n, m = map(int, input().split())
    
    if n==1 or m==1:
        print(0)
    else:
        print(2 * (min(n,m) - 1))