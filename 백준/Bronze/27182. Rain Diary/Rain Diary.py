n, m=map(int, input().split())

x=14+m-n
mm=m+7
if mm>x:
    mm-=x
print(mm)