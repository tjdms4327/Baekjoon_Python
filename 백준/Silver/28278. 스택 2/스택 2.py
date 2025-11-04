# silverIV_28278
import sys
input = sys.stdin.readline

stack = []

n = int(input())
for _ in range(n):
    cmd = input().strip().split()

    if cmd[0] == '1':     
        stack.append(int(cmd[1]))
    elif cmd[0] == '2':  
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == '3':    
        print(len(stack))
    elif cmd[0] == '4':       
        print(0 if stack else 1)
    elif cmd[0] == '5':     
        if stack:
            print(stack[-1])
        else:
            print(-1)
