n,w,h,l=map(int,input().split())
a=(w//l)*(h//l)
if a<=n:
    print(a)
else:
    print(n)