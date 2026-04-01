# bronzeIII_13617
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 선수 수, 경기 수
count = 0
for _ in range(n):
    player = list(map(int, input().split()))
    if 0 not in player:
        count += 1
print(count)