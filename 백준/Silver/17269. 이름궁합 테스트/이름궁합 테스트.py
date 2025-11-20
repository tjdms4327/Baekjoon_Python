# silverV_17269
import sys
input = sys.stdin.readline

mapping = {'A':3, 'B':2, 'C':1, 'D':2, 'E':4,
           'F':3, 'G':1, 'H':3, 'I':1, 'J':1,
           'K':3, 'L':1, 'M':3, 'N':2, 'O':1,
           'P':2, 'Q':2, 'R':2, 'S':1, 'T':2, 
           'U':1, 'V':1, 'W':1, 'X':2, 'Y':2, 'Z':1}

n, m = map(int, input().split())
name1, name2 = input().strip().split()

names = []
min_len = min(n, m)
for i in range(min_len):
    names.append(mapping[name1[i]])
    names.append(mapping[name2[i]])
if n < m:
    for i in range(n, m):
        names.append(mapping[name2[i]])
elif n > m:
    for i in range(m, n):
        names.append(mapping[name1[i]])
        
while len(names) > 2:
    names = [(names[i]+names[i+1])%10 for i in range(len(names)-1)]
score = names[0]*10+names[1]
print(f'{score}%')