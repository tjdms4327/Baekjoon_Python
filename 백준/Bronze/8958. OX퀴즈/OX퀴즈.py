t=int(input())
for _ in range(t):
    a=input()
    tot=0
    n=1
    for i in a:
        if i=='O':
            tot+=n
            n+=1
        else:
            n=1
    print(tot)