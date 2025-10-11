# bronzeIII_9924
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
count = 0
while a != b:
    a, b = max(a, b)-min(a, b), min(a, b)
    count += 1
print(count)