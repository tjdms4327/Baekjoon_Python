a=map(int,input().split())
mul=0
for i in a:
    mul+=(i**2)
print(int(mul%10))