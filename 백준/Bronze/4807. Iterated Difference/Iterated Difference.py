import sys
input = sys.stdin.readline

case = 0
while True:
    n = int(input())
    if n == 0:
        break
    
    case += 1
    lst = list(map(int, input().split()))
    count = 0
    ok = True
    while len(set(lst))!=1:
        lst += [lst[0]]
        lst = [abs(lst[k] - lst[k+1]) for k in range(len(lst)-1)]
        count += 1
        
        if count > 1000:
            ok = False
            break
    if ok:
        print(f'Case {case}: {count} iterations')
    else:
        print(f'Case {case}: not attained')