import sys 
input = sys.stdin.readline

snacks = [list(map(int, input().split()))
        for _ in range(3)]


max_v = []
for i in range(3):
    cur = snacks[i]
    cost = 10 * cur[0]
    val = (10*cur[1]) / (cost - (500 if cost>=5000 else 0))
    max_v.append(val)

name = ['S', 'N', 'U']
idx = max_v.index(max(max_v))
print(name[idx])