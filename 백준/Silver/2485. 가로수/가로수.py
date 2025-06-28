import math

n=int(input())
pos=[int(input()) for _ in range(n)]
tree=[pos[i+1]-pos[i] for i in range(n-1)]

gcd=math.gcd(*tree)
print((pos[-1]-pos[0])//gcd-n+1)