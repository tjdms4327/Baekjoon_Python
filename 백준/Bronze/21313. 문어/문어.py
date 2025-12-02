import sys
input = sys.stdin.readline

n = int(input())
print(*([1, 2] * (n//2)) + ([3] if n%2==1 else []))