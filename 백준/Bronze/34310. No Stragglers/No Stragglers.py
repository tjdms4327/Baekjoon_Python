# bronzeIII_34310
import sys
input = sys.stdin.readline

people = 0
n = int(input())
for _ in range(n):
    a, b, c = input().strip().split()
    if b == 'IN':
        people += int(c)
    else:
        people -= int(c)
print(people if people else 'NO STRAGGLERS')