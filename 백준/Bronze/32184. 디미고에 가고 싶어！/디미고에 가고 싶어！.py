import sys
input = sys.stdin.readline

a, b = map(int, input().split())
picture = 0
if a % 2 == 0:
    picture += 1
    a += 1
if b % 2 == 1:
    picture += 1
    b -= 1
picture += (b - a + 1) // 2
print(picture)