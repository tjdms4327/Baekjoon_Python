import math

S=int(input())
A=int(input())
B=int(input())

pay=250
if S>A:
    height=S-A
    pay += math.ceil(height/B)*100
print(pay)