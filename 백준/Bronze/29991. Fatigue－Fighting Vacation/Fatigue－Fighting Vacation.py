import sys
input = sys.stdin.readline

d, c, r = map(int, input().split())
C = [int(input()) for _ in range(c)]
R = [int(input()) for _ in range(r)]

count = 0
while True:
    if C and d >= C[0]:
        d -= C.pop(0)
        count += 1
    elif R:
        d += R.pop(0)
        count += 1
    else:
        break

print(count)