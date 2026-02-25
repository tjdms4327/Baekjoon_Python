import sys
input = sys.stdin.readline

rock = [1, 2, 3]
count = [0]*3

n = int(input())
for _ in range(n):
    a, b, g = map(int, input().split())
    rock[a-1], rock[b-1] = rock[b-1], rock[a-1]
    count[rock[g-1]-1] += 1
    
print(max(count))