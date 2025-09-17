import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

sum = n
for _ in range(k):
    sum *= 10
    sum += n
print(sum)