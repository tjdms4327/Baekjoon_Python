import sys
input=sys.stdin.readline

n=int(input())
stops=[list(map(int, input().split())) for _ in range(n)]
stops.sort(key=lambda x:x[1])
print(*stops[0])