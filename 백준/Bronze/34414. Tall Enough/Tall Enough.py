import sys
input = sys.stdin.readline

n = int(input())
height = [int(input()) for _ in range(n)]

if any(x < 48 for x in height):
    print('False')
else:
    print('True')