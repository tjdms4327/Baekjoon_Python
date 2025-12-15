import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, 1+n):
    s = list(input().strip().split())
    
    result = []
    for word in s:
        if len(word) == 4:
            result.append('*'*4)
        else:
            result.append(word)
            
    print(*result)
    if i != n:
        print()