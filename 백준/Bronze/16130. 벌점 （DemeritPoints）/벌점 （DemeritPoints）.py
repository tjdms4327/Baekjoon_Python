# bronzeI_16130
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = list(input().strip())
    
    count = 0
    cum = 0
    weapon, o9 = False, False
    for i in s:
        prev = cum
        if '0'<=i<='9':
            cum += int(i)
        else:
            cum += ord(i) - ord('A') + 10
        
        if prev//10 < cum//10:
            week = cum//10
            if week <= 3:
                count += week
            elif week == 4:
                weapon = True
                break
            else:
                o9 = True
                break
    
    if weapon:
        print(f'{count}(weapon)')
    elif o9:
        print(f'{count}(09)')
    else:
        print(count)