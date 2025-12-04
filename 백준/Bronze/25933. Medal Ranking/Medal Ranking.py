import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    medal = list(map(int, input().split()))
    print(*medal)
    
    usa = medal[:3]
    russia = medal[3:]
    
    count = sum(usa) > sum(russia)
    color = False
    for i in range(3):
        if usa[i] > russia[i]:
            color = True
            break
        elif usa[i] < russia[i]:
            break
    
    if count and color:
        print('both')
    elif count:
        print('count')
    elif color:
        print('color')
    else:
        print('none')
    print()