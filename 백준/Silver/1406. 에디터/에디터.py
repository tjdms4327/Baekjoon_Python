# silverII_1406
import sys
input = sys.stdin.readline

left = list(input().strip())  
right = []  

m = int(input())
for _ in range(m):
    command = input().split()
    if command[0] == 'L':
        if left:
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'B':
        if left:
            left.pop()
    elif command[0] == 'P':
        left.append(command[1])

print(''.join(left + right[::-1]))
