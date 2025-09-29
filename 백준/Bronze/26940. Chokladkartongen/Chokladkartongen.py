# bronzeIII_26940
import sys
input = sys.stdin.readline

n = int(input())
chocolate = list(map(int, input().split()))

count = 0
for i in range(1, n):
    if chocolate[i-1] < chocolate[i]:
        count += 1
print(count)