# bronzeIII_32661
import sys
input = sys.stdin.readline

n = int(input())
fee = [int(input()) for _ in range(n)]

net_cost = int(min(fee) - max(fee)/2)
print(max(0, net_cost))