import sys
input = sys.stdin.readline

n, r, s = map(int, input().split())
for _ in range(n):
    nfp = []
    for i in range(r):
        row = input().strip()
        for j in row:
            if j == '#':
                nfp.append(r - i)
    print(max(nfp) - min(nfp))