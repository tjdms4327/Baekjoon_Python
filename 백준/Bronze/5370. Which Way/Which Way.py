import sys

for line in sys.stdin.read().splitlines():
    n = int(line)
    
    bin_n = bin(n)
    len_n = len(bin_n) - 2
    one = bin_n.count('1')
    zero = len_n - one
    
    if zero > one:
        print('left')
    elif zero == one:
        print('straight')
    else:
        print('right')