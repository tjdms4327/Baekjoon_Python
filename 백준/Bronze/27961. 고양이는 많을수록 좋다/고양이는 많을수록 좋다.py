import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
    sys.exit()
    
current, count = 1, 1
while current < n:
    current *= 2
    count += 1
print(count)