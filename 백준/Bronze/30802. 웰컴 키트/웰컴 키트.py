import math

n=int(input())
size=list(map(int, input().split()))
t,p=map(int, input().split())

t_shirt=[math.ceil(i/t) for i in size]
print(sum(t_shirt))
print(n//p, n%p)