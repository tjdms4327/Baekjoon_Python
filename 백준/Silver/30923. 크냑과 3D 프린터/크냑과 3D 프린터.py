import sys
input = sys.stdin.readline

n = int(input())
H = list(map(int, input().split()))

area = 2*n + H[0] + H[-1] + 2*sum(H)
for i in range(1, n):
    area += abs(H[i]-H[i-1])
print(area)