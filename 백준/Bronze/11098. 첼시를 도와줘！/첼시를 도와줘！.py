n=int(input()) 
for _ in range(n):
    name=[] ; cost=[]
    for _ in range(int(input())):
        b,a=input().split()
        name.append(a) ; cost.append(int(b))
    idx=cost.index(max(cost))
    print(name[idx])