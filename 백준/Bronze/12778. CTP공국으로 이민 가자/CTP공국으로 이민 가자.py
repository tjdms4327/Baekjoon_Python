import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, problem = input().strip().split()
    
    ans = []
    if problem == 'C':
        code = list(input().strip().split())
        for i in code:
            ans.append(ord(i) - ord('A') + 1)
    else:
        code = list(map(int, input().split()))
        for i in code:
            ans.append(chr(ord('A')+i-1))
    
    print(*ans)