# bronzeI_1373
import sys
input = sys.stdin.readline

n = int(input().strip(), 2)

oct_n = oct(n)
print(oct_n[2:])