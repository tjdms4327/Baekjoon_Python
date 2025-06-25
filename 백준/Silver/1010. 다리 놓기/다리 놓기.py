t=int(input())

def fac(x):
    a=1
    for i in range(1,x+1):
       a*=i
    return a

for _ in range(t):
    n,m=map(int,input().split())
    nn=fac(n) ; mm=fac(m) ; mn=fac(m-n)
    print(mm//(nn*mn))