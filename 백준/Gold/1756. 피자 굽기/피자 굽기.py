import sys
input = sys.stdin.readline

d, n = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

oven_poss = oven[:]
for i in range(1, d):
    oven_poss[i] = min(oven_poss[i], oven_poss[i-1])

idx = d
for p in pizza:
    while oven_poss[idx-1] < p:
        idx -= 1
        if idx < 0:
            print(0)
            sys.exit()
    idx -= 1
    

print(idx+1) # 마지막 위치에서 1 뺀거 복구