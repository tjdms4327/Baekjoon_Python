# bronzeII_1075
import sys
input = sys.stdin.readline

n = int(input())
f = int(input())

slice_n = (n//100)*100
for a in range(10):
    for b in range(10):
        last_digit2 = 10*a + b
        new_n = slice_n + last_digit2
        if new_n % f == 0:
            print(f'{last_digit2:02d}')
            exit()