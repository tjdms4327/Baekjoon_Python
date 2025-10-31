import sys
input = sys.stdin.readline

g = 9.81

k = int(input())
for case in range(1, k+1):
    n, M = map(float, input().split())
    n = int(n)
    stages = [tuple(map(float, input().split())) for _ in range(n)]
    
    mass = M + sum(stage[0] for stage in stages)
    height = 0.0
    velocity = 0.0
    
    for mi, ti, Fi in stages:
        a = Fi / mass - g
        height += velocity * ti + 0.5 * a * ti**2
        velocity += a * ti
        mass -= mi
    
    print(f'Data Set {case}:')
    print(f'{height:.2f}')
    print()   
