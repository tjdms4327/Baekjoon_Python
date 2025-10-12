# silverIV_15821
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

D = []
for _ in range(n):
    p = int(input())
    xy = list(map(int, input().split()))
    
    max_distance = 0
    for i in range(0, p*2, 2):
        distance =(xy[i]**2 + xy[i+1]**2)
        max_distance = max(max_distance, distance)
    D.append(max_distance)
D.sort()
print(f'{D[k-1]:.2f}')