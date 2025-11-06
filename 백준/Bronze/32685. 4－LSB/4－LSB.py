# bronzeII_32685
import sys
input = sys.stdin.readline

a = format(int(input()), '04b')[-4:]
b = format(int(input()), '04b')[-4:]
c = format(int(input()), '04b')[-4:]

ans = a + b + c
print(str(int(ans, 2)).zfill(4))