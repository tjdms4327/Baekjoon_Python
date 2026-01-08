import sys
input = sys.stdin.readline

n = int(input())
L = list(input().strip().split())

for i in range(1, n//2+1):
    if L[:i] == L[-i:]:
        print('yes')
        sys.exit()
        
print('no')