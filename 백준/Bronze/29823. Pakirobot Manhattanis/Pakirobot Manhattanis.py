def move(n, s):
    x,y=0,0
    for i in range(n):
        if s[i]=='N':
            y+=1
        elif s[i]=='S':
            y-=1
        elif s[i]=='E':
            x+=1
        elif s[i]=='W':
            x-=1
    return abs(x)+abs(y)

n=int(input())
s=input()
print(move(n,s))