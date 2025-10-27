# bronzeII_29716
import sys, re
input = sys.stdin.readline

j, n = map(int, input().split())
count = 0
for _ in range(n):
    s = input().strip()
    
    upper = len(re.findall(r'[A-Z]', s))
    lower = len(re.findall(r'[a-z]', s))
    digit = len(re.findall(r'[0-9]', s))
    space = len(re.findall(r'\s', s))
    
    score = 4 * upper + 2 * (lower + digit) + space
    if score <= j:
        count += 1

print(count)