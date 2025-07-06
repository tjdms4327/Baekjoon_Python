import sys
input=sys.stdin.readline
from collections import deque

def command():
    c=input().split()
    if len(c)==2:
        x=int(c[-1])
        if c[0]=='push_front':
            dq.appendleft(x)
        elif c[0]=='push_back':
            dq.append(x)
    else:
        if c[0]=='empty':
            if dq:
                print(0)
            else:
                print(1)
        elif c[0]=='size':
            print(len(dq))
        else:
            if not dq:
                print(-1)
            elif c[0]=='pop_front':
                print(dq.popleft())
            elif c[0]=='pop_back':
                print(dq.pop())
            elif c[0]=='front':
                print(dq[0])
            elif c[0]=='back':
                print(dq[-1])


n=int(input())
dq=deque([])
for _ in range(n):
    command()