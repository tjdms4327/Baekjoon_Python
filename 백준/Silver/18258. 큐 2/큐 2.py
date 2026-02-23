import sys
input = sys.stdin.readline
from collections import deque

def command(line):
    s = line[0]
    if s == 'push':
        lst.append(line[1])
    elif s == 'pop':
        if lst:
            print(lst.popleft())
        else:
            print(-1)
    elif s == 'size':
        print(len(lst))
    elif s == 'empty':
        print(0 if lst else 1)
    elif s == 'front':
        print(lst[0] if lst else -1)
    elif s == 'back':
        print(lst[-1] if lst else -1)

lst = deque()

n = int(input())
for _ in range(n):
    line = input().split()
    command(line)