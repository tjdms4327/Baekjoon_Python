min_o, tot= 101, 0
for _ in range(7):
    num=int(input())
    if num%2==1:
        tot+=num
        if num<min_o:
            min_o=num

if tot==0:
    print(-1)
else:
    print(tot)
    print(min_o)