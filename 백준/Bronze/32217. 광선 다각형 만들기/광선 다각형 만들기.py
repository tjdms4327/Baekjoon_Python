import sys
input = sys.stdin.readline

n = int(input())
angles= list(map(int, input().split()))

print(180*(n-1) - 2*sum(angles))