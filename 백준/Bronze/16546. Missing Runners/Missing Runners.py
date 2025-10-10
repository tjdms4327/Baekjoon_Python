# bronzeIII_16546
import sys
input = sys.stdin.readline

n = int(input())
cross_line = set(map(int, input().split()))

all_player = set(range(1, n+1))
print(*(all_player - cross_line))