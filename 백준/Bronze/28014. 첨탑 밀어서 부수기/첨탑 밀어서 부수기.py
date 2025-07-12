import sys
input=sys.stdin.readline

n=int(input().strip())
H=list(map(int, input().strip().split()))

cnt=1 # 첫번째는 무조건 밀어야 함
for i in range(n-1):
    if H[i]<=H[i+1]:
        cnt+=1

print(cnt)