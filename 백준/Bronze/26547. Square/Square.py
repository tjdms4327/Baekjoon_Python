import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().strip()
    length = len(s)

    print(s)
    for i in range(1, length-1):
        print(s[i] + ' '*(length-2) + s[-(i+1)])
    if length > 1:
        print(s[::-1])