# bronzeII_1681
import sys
input = sys.stdin.readline

n, l = input().strip().split()
n = int(n)

label = 0
while n > 0:
    label += 1
    while l in str(label):
        label += 1
    n -= 1
print(label)