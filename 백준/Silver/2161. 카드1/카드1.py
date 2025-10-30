# silverV_2161
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
myQueue = deque(range(1,n+1))

while len(myQueue) > 1:
    print(myQueue.popleft(), end=' ')
    
    data = myQueue.popleft()
    myQueue.append(data)
print(myQueue.popleft())