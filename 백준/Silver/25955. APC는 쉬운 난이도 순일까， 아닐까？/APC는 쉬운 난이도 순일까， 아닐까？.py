import sys
input = sys.stdin.readline

n = int(input())
levels = list(input().strip().split())

tier_order = {'B': 0, 'S': 1, 'G': 2, 'P': 3, 'D': 4}
def key_func(problem):
    tier = problem[0]
    level = int(problem[1:])
    return (tier_order[tier], -level)

sorted_levels = sorted(levels, key=key_func)
if levels == sorted_levels:
    print('OK')
else:
    print('KO')
    for i in range(n):
        if levels[i] != sorted_levels[i]:
            print(sorted_levels[i], end=' ')