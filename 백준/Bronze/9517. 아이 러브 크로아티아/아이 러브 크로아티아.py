import sys
input = sys.stdin.readline

k = int(input())
n = int(input())

left_time = 3 * 60 + 30
for _ in range(n):
    t, z = input().strip().split()
    t = int(t)
    
    if left_time <= t:
        break
        
    if z == 'T':
        k = (k % 8) + 1
    left_time -= t
    
print(k)
    