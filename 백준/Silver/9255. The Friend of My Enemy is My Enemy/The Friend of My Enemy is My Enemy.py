import sys
input = sys.stdin.readline

k = int(input())
for case in range(1,1+k):
    n, m = map(int, input().split())
    
    graph = [set() for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
        
    start = int(input())
    
    print(f'Data Set {case}:')
    print(*sorted(graph[start]))
    print()