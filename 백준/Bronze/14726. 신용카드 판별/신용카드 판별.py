t=int(input())
for _ in range(t):
    s=input()
    tot=0
    for i in range(15, -1, -1):
        temp=int(s[i])
        if i%2==0:
            temp*=2
            if temp>=10:
                temp=temp//10+temp%10
        tot+=temp

    if tot%10==0: print('T')
    else: print('F')