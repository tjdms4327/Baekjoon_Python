# bronzeIII_21280
import sys
input = sys.stdin.readline

n = int(input())
lecture = list(map(int, input().split()))

absent_plus = [0, 0]
for i in range(1, n):
    a = lecture[i - 1]
    diff = lecture[i] - a
    if diff < 0:
        absent_plus[0] -= diff
    elif diff > 0:
        absent_plus[1] += diff
print(*absent_plus)