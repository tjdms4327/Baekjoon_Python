a,b,c,x,y=map(int, input().split())

chick=min(x,y)
if x>=y: k=a
else: k=b
print(min(a*x+b*y, chick*2*c+abs(x-y)*k, a*x+2*c*y, b*y+2*c*x, max(x,y)*2*c))