import sys
input = sys.stdin.readline
output = []

n = int(input())
s = []

for _ in range(n):
    words = input().split()
    
    if words[0] == 'push':
        s.append(words[1])
    
    elif words[0] == 'pop':
        if s: output.append(s.pop())
        else: output.append(-1)
    
    elif words[0] == 'size':
        output.append(len(s))
    
    elif words[0] == 'empty':
        if s: output.append(0)
        else: output.append(1)
    
    elif words[0] == 'top':
        if s: output.append(s[-1])
        else: output.append(-1)

sys.stdout.write("\n".join(map(str, output)) + "\n")
