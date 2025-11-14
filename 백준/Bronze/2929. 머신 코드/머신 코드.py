# bronzeI_2929
import sys
input = sys.stdin.readline

s = input().strip()

index_upper = [i for i in range(len(s)) if s[i].isupper()]
count_NOP = 0
for i in range(1, len(index_upper)):
    diff = index_upper[i] - index_upper[i-1]
    if diff % 4 != 0:
        count_NOP += (diff//4+1)*4 - diff
print(count_NOP)