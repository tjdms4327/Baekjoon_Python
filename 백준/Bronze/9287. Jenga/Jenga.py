import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, 1+t):
    h = int(input())
    jenga = [input().strip() for _ in range(h)]
    
    result = "Standing"
    for row in jenga:
        if '00' in row:
            result = 'Fallen'
            break
    print(f'Case {case}: {result}')