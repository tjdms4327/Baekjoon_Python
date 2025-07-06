n=int(input())

xy=[]
for i in range(n):
    x,y=(map(int, input().split()))
    xy.append([y,x])
xy.sort()

for i in xy:
    print(i[1], i[0])