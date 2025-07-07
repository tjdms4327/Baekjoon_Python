import math

n=int(input())
for _ in range(n):
    a1, p1=map(int, input().split())
    r1, p2=map(int, input().split())

    slice=a1/p1
    Whole=r1*r1*math.pi/p2
    if slice>Whole:
        print('Slice of pizza')
    else:
        print('Whole pizza')