import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s1 = n * (n+1) // 2
    s2 = n * n
    s3 = n * (n+1)
    print(s1, s2, s3)