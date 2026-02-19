import sys
input = sys.stdin.readline

n = int(input())

time = {}

time_mapping = {0:4, 1:6, 2:4, 3:10}
for week in range(n):
    for i in range(4):
        s = list(input().strip().split())
        
        t = time_mapping[i]
        for x in s:
            if x != '-':
                time[x] = time.get(x, 0) + t
                

if not time or max(time.values()) - min(time.values()) <= 12:
    print('Yes')
else:
    print('No')