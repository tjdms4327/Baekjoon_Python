# bronzeIV_34552
import sys
input = sys.stdin.readline

M = list(map(int, input().split()))
n = int(input()) # 학생 수
total = 0
for _ in range(n):
    b, l, s = map(float, input().split())
    if l >= 2.0 and s >= 17:
        total += M[int(b)]
print(total)