x,y=map(float, input().split())

n=int(input())
for _ in range(n):
    xi,yi=map(float, input().split())
    if x/y>xi/yi:
        x,y=xi,yi
print(x/y*1000)