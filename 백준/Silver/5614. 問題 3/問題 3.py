import sys
input = sys.stdin.readline

n = int(input())

dic = {}
for _ in range(n):
    name, val = input().split()
    val = int(val)
    if name in dic:
        dic[name] += val
    else:
        dic[name] = val


items = sorted(dic.items(), key=lambda x: (len(x[0]), x[0]))
for name, total in items:
    print(name, total)
