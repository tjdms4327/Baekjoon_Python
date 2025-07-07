mouse=list(map(int,input().split()))
mouse.sort()

print(sum(mouse[1:])+1)