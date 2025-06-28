h,m=map(int,input().split())
time=int(input())
new_m=m+time

if h+(new_m//60)>=24:
    print(h+(new_m//60)-24, new_m-(new_m//60)*60)
else:
    print(h+(new_m//60), new_m-(new_m//60)*60)