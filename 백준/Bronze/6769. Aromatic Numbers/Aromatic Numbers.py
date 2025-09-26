# bronzeII_6769
import sys
input = sys.stdin.readline

mapping = {'I':1, 'V':5, 'X':10, 'L':50,
           'C':100, 'D':500, 'M':1000}  

s = input().strip()

pairs = [(int(s[i]), mapping[s[i+1]]) for i in range(0, len(s), 2)]
total = 0
for i in range(len(pairs)):
    val = pairs[i][0] * pairs[i][1]
    if i+1 < len(pairs) and pairs[i][1] < pairs[i+1][1]:
        total -= val
    else:
        total += val
print(total)