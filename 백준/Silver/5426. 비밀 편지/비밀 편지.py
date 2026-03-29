import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    n = int(len(s) ** 0.5)
    
    matrix = [s[i:i+n] for i in range(0, len(s), n)]
    
    ans = ''
    for col in zip(*matrix):
        ans = ''.join(col) + ans
        
    print(ans)