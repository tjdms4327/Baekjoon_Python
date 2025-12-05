import sys
input = sys.stdin.readline

r, s, n = map(int, input().split())
A = list(map(int, input().split()))

if r % s == 0:
    print(0)
    sys.exit()
total = 0
for i, a in enumerate(A, start=1):
    total += a
    if (total - r) % s == 0:
        print(i)
        sys.exit()
print(-1)