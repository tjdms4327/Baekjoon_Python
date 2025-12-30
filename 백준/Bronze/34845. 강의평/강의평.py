import sys
input = sys.stdin.readline

n, x = map(int, input().split())
A = list(map(int, input().split()))

A_sum = sum(A)
count100 = 0
while A_sum / (n+count100) < x:
    A_sum += 100
    count100 += 1
print(count100)