import sys
input = sys.stdin.readline

n = int(input())
A = set(list(map(int, input().split())))

for x in A:
    if (x+3 in A) and (x+6 in A):
        print('Yes')
        sys.exit()
print('No')