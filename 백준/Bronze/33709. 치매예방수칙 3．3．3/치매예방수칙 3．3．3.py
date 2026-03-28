import sys, re
input = sys.stdin.readline

n = int(input())
line = input().strip()

lst = re.split(r'[.|:#]', line)

ans = 0
for x in lst:
    ans += int(x)
    
print(ans)
