# bronzeI_17288
import sys
input = sys.stdin.readline

s = input().strip()

count = 0
length = 1 
for i in range(1, len(s)):
    if int(s[i-1]) + 1 == int(s[i]):
        length += 1
    else:
        if length == 3:
            count += 1
        length = 1
if length == 3:
    count += 1

print(count)
