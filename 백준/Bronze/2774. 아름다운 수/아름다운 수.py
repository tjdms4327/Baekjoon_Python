# bronzeII_2774
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x = set(map(int, input().strip()))
    print(len(x))