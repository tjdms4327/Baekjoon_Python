import sys
input=sys.stdin.readline

n=int(input())
count=0
for _ in range(n):
    ab=list(input().strip())
    stack=[]
    for i in ab:
        if stack and i==stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        count+=1
print(count)
        
    