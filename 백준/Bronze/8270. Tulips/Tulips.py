import sys
input = sys.stdin.readline

n = int(input())
tulips = set(map(int, input().split()))
print(15000 - len(tulips))