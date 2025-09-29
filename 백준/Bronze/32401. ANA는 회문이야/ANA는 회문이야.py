# bronzeII_32401
import sys
input = sys.stdin.readline

length = int(input())
s = input().strip()
count = 0
for i in range(length-2):
    for j in range(i+3, length+1):
        chunk = s[i:j]
        if (chunk[0] == chunk[-1] == 'A' and chunk.count('A') == 2) and (chunk.count('N') == 1):
            count += 1
print(count)