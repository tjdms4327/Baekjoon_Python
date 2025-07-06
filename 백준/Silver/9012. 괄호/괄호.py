T=int(input())

for _ in range(T):
    stack=[]
    bracket=input()
    for i in bracket:
        if i=='(':
            stack.append(i)
        elif i==')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack)==0:
            print('YES')
        else:
            print('NO')