import sys
input=sys.stdin.readline

x=int(input().strip())
for i in range(x+1, 10000):
    a=i//100
    b=i%100
    if (a+b)**2==i:
        print(i)
        break
else:
    print(-1)