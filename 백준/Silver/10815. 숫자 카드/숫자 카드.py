n=int(input())
sang=set(input().split())

m=int(input())
nums=list(input().split())
for i in nums:
    if i in sang:
        print(1, end=' ')
    else:
        print(0, end=' ')