import math

N, A, B, C, D=map(int, input().split())

pay=min(math.ceil(N/A)*B, math.ceil(N/C)*D)
print(pay)