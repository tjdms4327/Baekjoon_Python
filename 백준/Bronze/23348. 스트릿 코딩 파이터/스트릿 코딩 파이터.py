scores = list(map(int, input().split()))
n = int(input())
max_team = 0
for _ in range(n):
    cur = 0
    for _ in range(3): # 동아리원이 3명
        abc = list(map(int, input().split()))
        cur += scores[0] * abc[0] + scores[1] * abc[1] + scores[2] * abc[2]
    if cur > max_team:
        max_team = cur
print(max_team)