l,p=map(int,input().split())
tot=l*p
a=list(map(int,input().split()))
k=[(i-tot) for i in a]
print(*k, sep=' ')