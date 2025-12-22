import sys
input = sys.stdin.readline

n = int(input())
matching = {}
for _ in range(n):
    name, year = input().strip().split()
    matching[year] = name

print(matching['2026'])