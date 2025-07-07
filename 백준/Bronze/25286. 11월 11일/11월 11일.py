T=int(input())

lastmonth_30=[5,7,10,12]
for _ in range(T):
    y,m=map(int, input().split())
    if m==3:
        if y%400==0 or (y%4==0 and y%100!=0):
            print(y, 2, 29)
        else:
            print(y, 2, 28)
    elif m==1:
        print(y-1, 12, 31)
    elif m in lastmonth_30:
        print(y, m-1, 30)
    else:
        print(y, m-1, 31)