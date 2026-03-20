import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

gis = [A[0]]
for a in A[1:]:
    if gis[-1] < a:
        gis.append(a)
        
print(len(gis))
print(*gis)