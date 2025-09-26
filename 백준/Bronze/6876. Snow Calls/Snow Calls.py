# bronzeII_6876
import sys
input = sys.stdin.readline

mapping = {'A':2, 'B':2, 'C':2,
           'D':3, 'E':3, 'F':3,
           'G':4, 'H':4, 'I':4,
           'J':5, 'K':5, 'L':5,
           'M':6, 'N':6, 'O':6,
           'P':7, 'Q':7, 'R':7, 'S':7,
           'T':8, 'U':8, 'V':8,
           'W':9, 'X':9, 'Y':9, 'Z':9}

t = int(input())
for _ in range(t):
    s = list(input().strip().replace('-', ''))
    result = ''
    for i in range(len(s)):
        if s[i].isalpha():
            result += str(mapping[s[i]])
        else:
            result += s[i]
    print(f'{result[:3]}-{result[3:6]}-{result[6:10]}')