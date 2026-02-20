import sys
input = sys.stdin.readline

n = int(input())
skills = input().strip()

count = 0
L_count = S_count = 0
for x in skills:
    if '1' <= x <= '9':
        count += 1
        
    elif x == 'L':
        L_count += 1
    elif x == 'S':
        S_count += 1
        
    elif x == 'R':
        if L_count > 0:
            L_count -= 1
            count += 1
        else:
            break
    elif x == 'K':
        if S_count > 0:
            S_count -= 1
            count += 1
        else:
            break

print(count)