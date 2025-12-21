import sys
input = sys.stdin.readline

n, m, p = map(int, input().split())

count = 0
for row in range(1, n+1):
    for col in range(1, m+1):
        if (row+col)*2 >= p:
            count += (n-row+1)*(m-col+1)
print(count)