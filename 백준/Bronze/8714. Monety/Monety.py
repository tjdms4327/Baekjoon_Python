import sys
input = sys.stdin.readline

n = int(input())
front = list(input().split()).count('0')
print(min(front, n-front))