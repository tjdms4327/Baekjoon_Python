s,d=map(int,input().split())
if (s+d)%2 != 0 or s<d:
    print(-1)
else:
    print((s+d)//2, (s-d)//2)