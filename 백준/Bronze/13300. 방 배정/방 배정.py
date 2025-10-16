# bronzeII_13300
import sys
input = sys.stdin.readline
from math import ceil

n, k = map(int, input().split())
student = [0]*(2*6)
for _ in range(n):
    s, y = map(int, input().split())
    student[2*(y-1) + s] += 1

room = sum(ceil(i/k) for i in student)
print(room)