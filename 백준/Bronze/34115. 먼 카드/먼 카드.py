import sys
input=sys.stdin.readline

n=int(input())
nums=list(map(int, input().split()))


max_distance=-1
for i in range(1, n+1):
    first=nums.index(i)
    second=nums.index(i, first+1) # 시작점 지정

    distance=second-first-1
    if distance>max_distance:
        max_distance=distance

print(max_distance)
