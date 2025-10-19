# bronzeI_2810
import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

cup_holder = 1 + n - s.count('LL')
print(min(n, cup_holder))