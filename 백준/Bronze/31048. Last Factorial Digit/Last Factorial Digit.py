t=int(input())
for _ in range(t):
    n=int(input())
    num=1
    for i in range(2, n+1):
        num*=i
        if num>=10:
            num%=10
    print(num)