import math

w,h=map(int, input().split())

square=w+h
diagonal=math.sqrt(w**2+h**2)
print(round(square-diagonal, 9))