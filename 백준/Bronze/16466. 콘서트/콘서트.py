import sys
input = sys.stdin.readline

n = int(input())
A = sorted(list(map(int, input().split())))

for idx, num in enumerate(A, start=1):
    if idx != num:
        print(idx)
        sys.exit()
print(n+1)