# silver_32979
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
t = int(input())
myQueue = deque(map(int, input().split()))
B = list(map(int, input().split()))

for b in B:
    for i in range(1, b+1):
        if i < b:
            data = myQueue.popleft()
            myQueue.append(data)
        else:
            print(myQueue[0], end=' ')