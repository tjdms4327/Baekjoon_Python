import sys
input = sys.stdin.readline

n = int(input())
first = [tuple(map(int, input().split())) for _ in range(n)]
second = [tuple(map(int, input().split())) for _ in range(n)]

first.sort()
second.sort()

print(second[0][0]-first[0][0], second[0][1]-first[0][1])
