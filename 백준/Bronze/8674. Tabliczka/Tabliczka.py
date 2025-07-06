choco=list(map(int, input().split()))
choco.sort()

if choco[-1]%2==0 or choco[0]%2==0:
    print(0)
else:
    print(choco[0])