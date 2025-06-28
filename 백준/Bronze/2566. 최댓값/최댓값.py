b=[]
for _ in range(9):
    a=list(map(int,input().split()))
    b.extend(a)

idx=b.index(max(b))
print(max(b))
print(idx//9+1, idx%9+1)