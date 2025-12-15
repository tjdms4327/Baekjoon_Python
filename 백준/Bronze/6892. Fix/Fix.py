import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = [input().strip() for _ in range(3)]
    fixfree = True
    for i in range(3):
        for j in range(3):
            if i!=j:
                x = s[i]
                if s[j].startswith(x) or s[j].endswith(x):
                    fixfree = False
                    break
    if fixfree:
        print('Yes')
    else:
        print('No')
            
                