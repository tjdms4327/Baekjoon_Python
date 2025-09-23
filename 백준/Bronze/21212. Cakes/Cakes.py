# bronzeIII_21212.py
import sys
input = sys.stdin.readline

n = int(input())
ingredient = [tuple(map(int, input().split()))for _ in range(n)]

min_cake = float('inf')
for i in ingredient:
    min_cake = min(min_cake, i[1]//i[0])
print(min_cake)