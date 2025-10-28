# bronzeI_17176
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
s = sorted(input().strip())

decode = ''
for x in nums:
    if x == 0:
        decode += ' '
    elif 1 <= x <= 26:
        decode += chr(x + ord('A') - 1)
    else:
        decode += chr(x + ord('a') - 27)

if sorted(decode) == s:
    print('y')
else:
    print('n')