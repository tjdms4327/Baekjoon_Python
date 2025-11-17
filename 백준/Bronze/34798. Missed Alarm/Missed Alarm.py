# bronzeIV_34798
import sys
input = sys.stdin.readline

a = list(map(int, input().strip().split(':')))
alarm = a[0]*60+a[1]
b = list(map(int, input().strip().split(':')))
wake = b[0]*60+b[1]

if alarm < wake:
    print('YES')
else:
    print('NO')