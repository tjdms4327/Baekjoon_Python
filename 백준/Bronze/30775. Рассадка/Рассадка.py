# bronzeIII_30775
import sys
input = sys.stdin.readline

m, k = map(int, input().split())
n = list(map(int, input().split()))

total_student = sum(n)
if total_student % m == 0:
    print(total_student//m)
else:
    print(total_student//m + 1)