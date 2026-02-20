import sys
input = sys.stdin.readline

n = int(input())

time = {}
time_mapping = [4, 6, 4, 10]

for _ in range(n):
    for i in range(4):
        row = input().split()
        t = time_mapping[i]
        for name in row:
            if name != '-':
                time[name] = time.get(name, 0) + t

if not time:
    print("Yes")
else:
    values = time.values()
    if max(values) - min(values) <= 12:
        print("Yes")
    else:
        print("No")