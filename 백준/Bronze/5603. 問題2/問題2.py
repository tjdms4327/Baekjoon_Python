# bronzeII_5603
import sys
input = sys.stdin.readline

def count_n(s):
    result = ''
    prev = ''
    count = 0
    for i in s:
        if i == prev:
            count += 1
        else:
            if prev:
                result += str(count) + prev
            prev = i
            count = 1
    result += str(count) + prev
    return result
            
n = int(input())
s = input().strip()

for _ in range(n):
    s = count_n(s)
print(s)