n=int(input())
x0=[]
y0=[]

for _ in range(n):
    x,y=map(int, input().split())
    x0.append(x)
    y0.append(y)
    
l_x=max(x0)-min(x0)
l_y=max(y0)-min(y0)
print(l_x*l_y)