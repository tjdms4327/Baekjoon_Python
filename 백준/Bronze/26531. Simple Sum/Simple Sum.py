formula=list(input().split())

num=[int(formula[i]) for i in range(0,5,2)]
if num[0]+num[1]==num[-1]:
    print('YES')
else:
    print('NO')