import sys
input = sys.stdin.readline

pattern = 'ABCBCDCDADAB'

n = int(input())
for _ in range(n):
    z = int(input())
    print(pattern[(z-1) % 12])