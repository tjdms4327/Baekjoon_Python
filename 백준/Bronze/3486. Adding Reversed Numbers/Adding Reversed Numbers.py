# bronzeII_3486
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = input().strip().split()
    sum = int(a[::-1]) + int(b[::-1])
    print(int(str(sum)[::-1]))