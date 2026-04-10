import sys
input = sys.stdin.readline

n, m = map(int, input().split())
names, limits = [], []
for _ in range(n):
    name, x = input().strip().split()
    names.append(name)
    limits.append(int(x))
    


def find(power):
    left = 0
    right = n-1
    while left <= right:
        mid = (left+  right) // 2
        if power <= limits[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return names[left]
    
for _ in range(m):
    power = int(input())
    print(find(power))