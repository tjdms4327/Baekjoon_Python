import sys
input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))
    if lst == [0]:
        break
    
    n = lst[0]
    meatballs = lst[1:]
    ok = False
    for i in range(n):
        left = sum(meatballs[:i])
        right = sum(meatballs[i:])
        
        if left == right:
            print(f'Sam stops at position {i} and Ella stops at position {i+1}.')
            ok = True
            break
    if not ok:
        print('No equal partitioning.')