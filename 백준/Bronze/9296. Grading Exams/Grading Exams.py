import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, t+1):
    l = int(input())
    correct = list(input().strip())
    test = list(input().strip())
    
    count = 0
    for i in range(l):
        if correct[i] != test[i]:
            count += 1
    print(f'Case {case}: {count}')