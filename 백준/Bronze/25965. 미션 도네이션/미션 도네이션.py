import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    donation = 0
    mission = int(input())
    KDA = [list(map(int, input().split())) for _ in range(mission)]
    k, d, a = map(int, input().split())
    for kda in KDA:
        sum = kda[0]*k - kda[1]*d + kda[2]*a
        if sum < 0: pass
        else: donation += (sum)
    print(donation)