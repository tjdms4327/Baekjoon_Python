import sys
input = sys.stdin.readline

n, x = map(int, input().split())
T = list(map(int, input().split()))

i = 0
while x <= T[i]:
    x += 1
    i = (i + 1) % n
print(i + 1)