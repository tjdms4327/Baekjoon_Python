import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
d, m = map(int, input().split())

delete = []
cur = ''
result = ''
for x in s:
    if x not in 'HYU':
        cur += x
    else:
        result += x
        if cur:
            delete.append(cur)
        cur = ''
        
if cur:
    delete.append(cur)
    
# 삭제
energy = 0
for x in delete:
    energy += min(d+m, len(x)*d)

if energy == 0:
    print('Nalmeok')
else:
    print(energy)
    

# HYU 개수
cnt = min(result.count('H'), result.count('Y'), result.count('U'))
if cnt == 0:
    print('I love HanYang University')
else:
    print(cnt)