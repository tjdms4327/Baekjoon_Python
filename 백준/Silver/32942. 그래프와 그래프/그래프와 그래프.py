import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

graph = [[] for _ in range(11)]
for x in range(1, 11):
    for y in range(1, 11):
        if a*x + b*y == c:
            graph[x].append(y)
        
for x in graph[1:]:
    if x:
        print(*sorted(x))
    else:
        print(0)