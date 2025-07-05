d,h,m=map(int,input().split())
if d<11:
    print(-1)
elif d==11 and h<11:
    print(-1)
elif d==11 and h==11 and m<11:
    print(-1)
else:
    d-=11 ; h-=11 ; m-=11
    print(d*60*24+h*60+m)