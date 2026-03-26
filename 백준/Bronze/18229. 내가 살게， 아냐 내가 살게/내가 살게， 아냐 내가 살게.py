import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

hand = [list(map(int, input().split())) for _ in range(n)]

cur = [0] * n
count = 0
for round in range(m):
    for person in range(n):
        cur[person] += hand[person][round]
        count += 1
        if cur[person] >= k:
            print(person+1, round+1)
            sys.exit()