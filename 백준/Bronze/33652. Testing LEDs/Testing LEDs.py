import sys
input = sys.stdin.readline

n = int(input())

light = []
for _ in range(n):
    m, o = map(int, input().split())
    light.append((o, m))
light.sort(key=lambda x:x[1])

for x, y in light:
    if x == 0:
        print(y)
        sys.exit()
print(-1)