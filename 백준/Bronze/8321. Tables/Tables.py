import sys
input = sys.stdin.readline

n, k, s = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

tot = k*s
for i in range(n):
    tot -= A[i]
    
    if tot <= 0:
        print(i+1)
        sys.exit()