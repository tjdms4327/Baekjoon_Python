n=int(input())
for _ in range(n):
    lll, dddd=input().split('-')
    val_l=sum((ord(lll[i])-ord('A'))*(26**(2-i)) for i in range(3))
    #print(val_l)
    
    if abs(val_l-int(dddd))<=100:
        print('nice')
    else:
        print('not nice')