# bronzeIII_21420
import sys
input = sys.stdin.readline

n = int(input())
coins = [int(input()) for _ in range(n)]

front = coins.count(1)
print(min(front, n-front))