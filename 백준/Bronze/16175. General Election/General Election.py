# bronzeIII_16175
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    vote = []
    for _ in range(m):
        vote.append(list(map(int, input().split())))

    result = [0] * (n+1)
    i = 1
    for x in zip(*vote):
        result[i] = sum(x)
        i += 1
    print(result.index(max(result)))