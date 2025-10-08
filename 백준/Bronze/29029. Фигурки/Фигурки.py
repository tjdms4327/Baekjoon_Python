# bronzeIII_29029
import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

direction = ['N', 'S', 'E', 'W']
count = [0]*4
for i in range(4):
    count[i] = s.count(direction[i])
print(n - max(count))