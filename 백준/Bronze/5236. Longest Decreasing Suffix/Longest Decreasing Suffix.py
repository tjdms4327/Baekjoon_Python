# bronzeII_5236
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().strip()
    
    result = s[-1]  # 마지막 문자는 항상 감소
    for i in range(len(s)-2, -1, -1):
        if s[i] > result[0]:
            result = s[i] + result
        else:
            break

    print(f'The longest decreasing suffix of {s} is {result}')