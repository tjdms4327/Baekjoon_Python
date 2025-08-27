import sys
input = sys.stdin.readline

n = int(input())
s = list(input().strip().split())


for i in range(n):
    if s[i] == 'mumble':
        continue
    elif int(s[i]) != (i+1):
        print("something is fishy")
        exit(0)
print("makes sense")