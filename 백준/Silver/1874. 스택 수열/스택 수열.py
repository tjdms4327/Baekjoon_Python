import sys
input=sys.stdin.readline

n=int(input())
sequence=[int(input()) for _ in range(n)]
stack=[]
push_pop=[]
current=1

for i in range(n):
    while current<=sequence[i]:
        stack.append(current)
        push_pop.append('+')
        current+=1

    if stack and sequence[i]==stack[-1]:
            stack.pop()
            push_pop.append('-')
    else:
        print('NO')
        break
else:
    print(*push_pop, sep='\n')