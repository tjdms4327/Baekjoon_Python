import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    line = input().strip().split()
    letter_bank = sorted(set(line[0]))
    s = sorted(set(line[1]))
        
    
    if letter_bank == s:
        print('YES')
    else:
        print('NO')