# bronzeII_1392
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
B = [int(input()) for _ in range(n)]
time_list = []
for i in range(n):
    time_list.extend([i+1]*B[i])

for _ in range(q):
    t = int(input())
    print(time_list[t])