import sys
input=sys.stdin.readline

line=list(map(int, input().split()))
line.sort()
print(min(line[:2])*min(line[2:]))