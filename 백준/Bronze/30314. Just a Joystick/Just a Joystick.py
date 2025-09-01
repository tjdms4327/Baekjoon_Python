import sys
input = sys.stdin.readline

n = int(input())
last = input().strip()
now = input().strip()

tot = 0
for i in range(n):
    a, b = ord(last[i]), ord(now[i])
    tot += min(abs(a - b), 26 - abs(a - b))
print(tot)