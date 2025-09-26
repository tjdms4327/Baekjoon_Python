# bronzeII_6783
import sys
input = sys.stdin.readline

n = int(input())
s = sys.stdin.read().strip().upper()

count_t, count_s = s.count('T'), s.count('S')
if count_t > count_s:
    print('English')
else:
    print('French')