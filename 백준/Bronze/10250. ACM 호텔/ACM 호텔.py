t=int(input())
for _ in range(t):
    h,w,n=map(int, input().split())
    height=n%h
    width=(n//h)+1

    if height==0:
        height=h
        width=n//h
    print(100*height+width)