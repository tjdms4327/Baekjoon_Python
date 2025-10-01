# bronzeIII_17884
import sys
input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))

line = [0] * (n-1)
for i in range(n-1):
    line[d[i]] = (i+2)
print(1, *line)