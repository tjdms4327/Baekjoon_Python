m=int(input())
re=1000-m

num=0
k=[500,100,50,10,5,1]
while re !=0:
    for i in k:
        if re>=i:
            a=re//i
            re-=(a*i)
            num+=a
        else:
            pass

print(num)