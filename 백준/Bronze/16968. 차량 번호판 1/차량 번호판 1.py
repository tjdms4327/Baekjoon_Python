# bronzeI_16968
import sys
input = sys.stdin.readline

s = input().strip()

count = 1
alpha, num = 26, 10
for i in range(len(s)):
    if s[i] == 'c':
        if i != 0 and s[i] == s[i-1]:
            count *= (alpha-1)
        else:
            count *= alpha
    else: # d
        if i != 0 and s[i] == s[i-1]:
            count *= (num-1)
        else:
            count *= num
print(count)
            