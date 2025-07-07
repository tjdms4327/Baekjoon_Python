n,x=map(int, input().split())

time=-1
for i in range(n):
    s,t=map(int, input().split())
    if s+t<=x and s>time:
        time=s
print(time)