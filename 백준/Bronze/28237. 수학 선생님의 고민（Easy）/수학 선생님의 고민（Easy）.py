import sys
input = sys.stdin.readline

n = int(input())

a, b, c = n, n+1, -n-2
if b**2 - 4*a*c < 0:
    print(-1)
else:
    temp = (b**2 - 4*a*c) ** 0.5
    x1 = (-b - temp) / (2*a)
    x2 = (-b + temp) / (2*a)
    
    for i in range(1, n+1):
        if n%i==0 and n%(n//i)==0:
            if (x1*i).is_integer() and (x2*(n//i)).is_integer():
                print(i, -int(x1*i), n//i, -int(x2*(n//i)))
                sys.exit()
    print(-1)