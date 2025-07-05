def find_arc(a,b,c):
    if a+b==c:
        return str(a)+'+'+str(b)+'='+str(c)
    elif a==b+c:
        return str(a)+'='+str(b)+'+'+str(c)
    elif a-b==c:
        return str(a)+'-'+str(b)+'='+str(c)
    elif a==b-c:
        return str(a)+'='+str(b)+'-'+str(c)
    elif a*b==c:
        return str(a)+'*'+str(b)+'='+str(c)
    elif a==b*c:
        return str(a)+'='+str(b)+'*'+str(c)
    elif a//b==c:
        return str(a)+'/'+str(b)+'='+str(c)
    else:
        return str(a)+'='+str(b)+'/'+str(c)


a,b,c=map(int,input().split())
print(find_arc(a,b,c))