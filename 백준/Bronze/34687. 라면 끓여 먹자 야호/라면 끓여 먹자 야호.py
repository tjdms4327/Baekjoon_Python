# bronzeIV_34687
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
if m*100 >= n*81:
    print('yaho')
else:
    print('no')