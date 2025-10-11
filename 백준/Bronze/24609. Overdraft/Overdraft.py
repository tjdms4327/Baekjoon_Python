# bronzeIII_24609
import sys
input = sys.stdin.readline

record = [0]
n = int(input())
for _ in range(n):
    t = int(input())
    record.append(record[-1] + t)
print(max(0, -min(record)))