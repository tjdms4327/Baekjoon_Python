# bronzeIII_29729
import sys
input = sys.stdin.readline

s, n, m = map(int, input().split())
lst = []
for i in range(n+m):
    command = int(input())
    if command == 1:
        if len(lst) == s:
            s *= 2
        lst.append(1)
    elif command == 0:
        lst.pop()

print(s)