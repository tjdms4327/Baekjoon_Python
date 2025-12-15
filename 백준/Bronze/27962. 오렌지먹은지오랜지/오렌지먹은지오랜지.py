import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
for i in range(n):
    front = s[:i]
    back = s[-i:]
    
    diff_count = 0
    for x in range(i):
        if front[x] != back[x]:
            diff_count += 1
    if diff_count == 1:
        print('YES')
        sys.exit()
print('NO')