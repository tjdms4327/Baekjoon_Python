from collections import deque
import sys
input = sys.stdin.readline
output = []

n = int(input())
q = deque()

for _ in range(n):
    words = input().split()
    
    if words[0] == 'push':
        q.append(words[1])  
    
    elif words[0] == 'pop':
        if q: output.append(q.popleft()) 
        else: output.append(-1)
    
    elif words[0] == 'size':
        output.append(len(q))
    
    elif words[0] == 'empty':
        if q: output.append(0)
        else: output.append(1)
    
    elif words[0] == 'front': 
        if q: output.append(q[0])  
        else: output.append(-1)
    
    elif words[0] == 'back':
        if q: output.append(q[-1]) 
        else: output.append(-1)

sys.stdout.write("\n".join(map(str, output)) + "\n")
