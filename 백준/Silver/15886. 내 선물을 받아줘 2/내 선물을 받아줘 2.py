import sys
input = sys.stdin.readline

n = int(input())
move = input().strip()

print(move.count('EW'))