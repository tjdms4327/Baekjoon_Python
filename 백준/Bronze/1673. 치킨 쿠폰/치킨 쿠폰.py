# bronzeII_1673
import sys

for line in sys.stdin.read().splitlines():
    n, k = map(int, line.split())
    
    chicken = 0  
    coupon = n
    while coupon >= k:
        new = coupon // k
        chicken += new
        coupon = coupon % k + new
    print(chicken + n)