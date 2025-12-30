import sys
input = sys.stdin.readline

k = input().strip()
a = k[k.index('.')+1:]

print('YES')
print(int(a), 10**len(a))