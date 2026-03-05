import sys
input = sys.stdin.readline

n = int(input())
s = int(input().strip(), 2)

gray = s ^ (s>>1)
print(format(gray, f'0{n}b'))