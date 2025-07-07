a1, a0=map(int, input().split())
c=int(input())
n0=int(input())

if c>=a1 and n0*c>=a1*n0+a0:
    print(1)
else:
    print(0)