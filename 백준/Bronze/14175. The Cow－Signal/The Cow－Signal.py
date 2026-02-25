import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
picture = [list(input().strip()) for _ in range(m)]

for row in picture:
    line = ''.join([i*k for i in row])
    for _ in range(k):
        print(line)