# bronzeI_25166
import sys
input = sys.stdin.readline

s, m = map(int, input().split())

if s <= 1023:
    print('No thanks')
else:
    need = s - 1023
    if m & need == need:
        print('Thanks')
    else:
        print('Impossible')