import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

rain = 0
for j in range(1, m+1):
    t, r = map(int, input().split())
    rain += r  # 1층은 항상 포함

    if rain > k:
        print(j, 1)
        sys.exit()

print(-1)