import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n = int(input())
buttons = [int(input()) for _ in range(n)]

result = abs(b-a) # 기본은 주파수 1MHz씩 이동
for x in buttons:
    cand = 1 + abs(x-b)
    result = min(result, cand)

print(result)