# silverV_26042
import sys
input = sys.stdin.readline
from collections import deque

myQueue = deque()


n = int(input())
max_student, cur = 0, 0
end = float('inf')
for _ in range(n):
    line = input().strip()
    if line[0] == '1':
        a, num = map(int, line.split())
        myQueue.append(num)
        cur += 1
        
        if max_student < cur:
            end = num
            max_student = cur
        elif max_student == cur:
            end = min(end, num)
        
    else: # line[0]==2
        cur -= 1
        myQueue.popleft()

print(max_student, end)