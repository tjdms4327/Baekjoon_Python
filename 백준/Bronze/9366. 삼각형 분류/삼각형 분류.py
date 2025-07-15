def triangle(lst):
    lst.sort()
    if sum(lst[:2])<=lst[-1]:
        print("invalid!")
    elif len(set(lst))==1:
        print("equilateral")
    elif len(set(lst))==2:
        print("isosceles")
    else:
        print("scalene")
    return 0

    
t=int(input())
for i in range(1, t+1):
    lst=list(map(int, input().split()))
    
    print(f'Case #{i}: ', end='')
    triangle(lst)
    