# bronzeIII_10406
import sys
input = sys.stdin.readline

w, n, p = map(int, input().split())

punch = list(map(int, input().split()))
print(sum(1 for i in punch if w <= i <= n))