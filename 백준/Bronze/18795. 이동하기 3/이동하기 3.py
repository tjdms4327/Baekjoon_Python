# bronzeII_18795
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trash = list(map(int, input().split())) + list(map(int, input().split()))

print(sum(trash))