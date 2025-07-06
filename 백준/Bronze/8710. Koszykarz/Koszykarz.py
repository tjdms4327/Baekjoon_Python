import math

K, W, M=map(int, input().split())

height=W-K
print(math.ceil(height/M))