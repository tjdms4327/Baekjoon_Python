import sys
input = sys.stdin.readline

l, a = map(int, input().split())
H = list(map(int, input().split()))

for i in range(1, l+1):
    diff = H[i] - H[i-1]
    if diff <= a:
        continue
    else:
        print('BUG REPORT')
        sys.exit()
print('POSSIBLE')