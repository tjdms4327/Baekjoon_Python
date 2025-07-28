t=int(input())
for i in range(t):
    n, x=map(int, input().split())
    print(f'Case {i+1}: {n%x}')