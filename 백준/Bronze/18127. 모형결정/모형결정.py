import sys
input = sys.stdin.readline

a, b = map(int, input().split())
side = [1]
temp = 1
for i in range(1, b+1):
    temp += (a-2)
    side.append(temp)
print(sum(side))