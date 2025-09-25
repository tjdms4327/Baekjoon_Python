# bronzeII_4841
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().strip()
    
    result = []
    prev = s[0]
    count = 1
    for i in s[1:]:
        if prev == i:
            count += 1
        else:
            result.append(str(count))
            result.append(prev)
            prev = i
            count = 1
    result.append(str(count)) # 마지막 요소 추가
    result.append(prev)
    print(''.join(result))