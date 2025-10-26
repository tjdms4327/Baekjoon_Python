# bronzeII_18238
import sys
input = sys.stdin.readline

s = input().strip()

time = 0
prev = 'A'
for curr in s:
    time += min(abs(ord(curr) - ord(prev)), 26 - abs(ord(curr) - ord(prev)))
    prev = curr
print(time)