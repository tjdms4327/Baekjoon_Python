a,b,c=map(int,input().split())
if b>=c:
    print(int((a*b)/c))
else:
    print(int((a/b)*c))