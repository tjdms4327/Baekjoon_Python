import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    P = list(input().strip())
    n = int(input())
    arr = input().strip()

    if n == 0:
        nums = deque()
    else:
        nums = deque(map(int, arr[1:-1].split(',')))
        
    rev = False
    error = False
    for command in P:
        if command == 'D':
            if nums:
                if rev:
                    nums.pop()
                else:
                    nums.popleft()
            else:
                error = True
                break
        elif command == 'R':
            if rev:
                rev = False
            else:
                rev = True
                
    if error:
        print('error')
    else:
        if rev:
            nums.reverse()
        print('[' + ','.join(map(str, nums)) + ']')