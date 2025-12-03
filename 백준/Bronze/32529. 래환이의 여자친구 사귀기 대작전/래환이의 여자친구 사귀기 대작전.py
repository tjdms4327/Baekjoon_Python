import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

temp = 0
for i in range(n-1, -1, -1):
    temp += A[i]
    if temp >= m:
        print(i+1)
        sys.exit()
print(-1)