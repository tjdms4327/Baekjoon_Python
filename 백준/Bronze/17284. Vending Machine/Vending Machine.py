import sys
input = sys.stdin.readline

button = list(map(int, input().split()))
mapping = {1:500, 2:800, 3:1000}
print(5000 - sum(mapping[x] for x in button))