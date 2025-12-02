import sys
input = sys.stdin.readline

s = []
idx = 0

while True:
    n = int(input())
    if n == 0:
        break
    
    left, right = [], []
    for _ in range(n):
        action = input().strip().split()
        cmd = action[0]
        
        if cmd == 'INSERT':
            left.append(action[1])
        elif cmd == 'LEFT' and left:
            right.insert(0, left.pop())
        elif cmd == 'RIGHT' and right:
            left.append(right.pop(0))
    print(''.join(left+right))