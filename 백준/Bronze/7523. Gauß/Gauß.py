import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, 1+t):
    n, m = map(int, input().split())
    
    result = (n+m)* (m-n+1)//2
    print(f'Scenario #{case}:\n{result}\n')