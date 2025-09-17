import sys
input = sys.stdin.readline

a, b, x, y = map(int, input().split())
start, end = min(a, b), max(a, b)
move = [min(x, y), max(x, y)]

option = [end - start, abs(start - move[0])+abs(move[-1] - end)]
print(min(option))