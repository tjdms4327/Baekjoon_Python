import sys
input = sys.stdin.readline

time = [0]*1001

n = int(input())
for _ in range(n):
    s, t, b = map(int, input().split())
    for i in range(s, t):
        time[i] += b

print(max(time))