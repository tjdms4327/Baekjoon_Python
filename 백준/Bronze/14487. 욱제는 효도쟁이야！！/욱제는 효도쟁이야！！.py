import sys
input=sys.stdin.readline

n=int(input().strip())
v=list(map(int, input().strip().split()))

max_vi=max(v)
print(sum(v)-max_vi)