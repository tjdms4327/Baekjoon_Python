import sys
input = sys.stdin.readline

n = int(input())
rule = {}
for _ in range(n):
    line = list(input().strip().split())
    x, Y = line[0], line[2:]
    rule[x] = Y

s = input().strip()
for i in range(0, len(s)-1):
    if s[i] in rule:
        if s[i+1] in rule[s[i]]:
            continue
        else:
            print('no')
            sys.exit()
print('yes')    