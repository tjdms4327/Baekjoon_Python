h,w,n,m=map(int, input().split())

row=(h+n)//(n+1)
col=(w+m)//(m+1)
print(row*col)