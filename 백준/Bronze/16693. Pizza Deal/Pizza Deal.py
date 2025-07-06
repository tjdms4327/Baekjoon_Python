import math

A, P1=map(int, input().split())
R, P2=map(int, input().split())

slice=P1/A
whole=P2/(R*R*math.pi)
if slice>whole:
    print("Whole pizza")
else:
    print("Slice of pizza")