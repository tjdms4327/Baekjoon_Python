p1, q1, p2, q2 = map(int, input().split())

if (p1*p2) % (2*q1*q2)==0:
    print(1)
else:
    print(0)