n,t=map(int, input().split())
works=list(map(int, input().split()))

for i in range(n,-1,-1):
    if sum(works[:i])<=t:
        print(i)
        break