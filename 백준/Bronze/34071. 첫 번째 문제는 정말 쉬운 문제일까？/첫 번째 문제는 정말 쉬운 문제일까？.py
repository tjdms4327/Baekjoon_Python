n=int(input())
levels=[int(input()) for _ in range(n)]
sort_levels=sorted(levels)
if levels[0]==sort_levels[0]:
    print('ez')
elif levels[0]==sort_levels[-1]:
    print('hard')
else:
    print('?')