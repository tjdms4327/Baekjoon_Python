# bronzeIII_30310
import sys
input = sys.stdin.readline

n = int(input())
fork = list(map(int, input().split()))
fork.sort()
print(fork[0] + fork[1])