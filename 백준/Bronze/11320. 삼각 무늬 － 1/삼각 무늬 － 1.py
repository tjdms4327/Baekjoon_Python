t=int(input())
for _ in range(t):
    a,b=map(int, input().split())
    side=(a//b)
    if a%b!=0:
        side+=1
    print(side**2)