t=int(input())

for _ in range(t):
    a, b=map(int, input().split())
    
    a_1=a%10
    if a_1==0:
        print(10)
    elif a_1 in [1, 5,6]:
        print(a_1)
    elif a_1 in [4,9]:
        if b%2!=0:
            print(a_1)
        else:
            print((a_1**2) %10)
    else:
        if b%4==0:
            print((a_1**4)%10)
        else:
            print((a_1)**(b%4)%10)