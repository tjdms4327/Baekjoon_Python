# bronzeII_11296
import sys
input = sys.stdin.readline

discount = {'R':.55, 'G':.7, 'B':.8,
           'Y':.85, 'O':.9, 'W':.95}

n = int(input())
for _ in range(n):
    price, dots, coupon, pay = input().strip().split()
    price = float(price)
    
    price *= discount[dots]
    if coupon == 'C':
        price *= 0.95
        
    if pay == 'P':  
        price = round(price + 1e-9, 2)
    else:
        scaled = price * 100
        second = int(scaled) % 10   
        first = int(scaled // 10)   
        if second >= 6:
            first += 1

        price = first / 10     
        price = round(price, 2)
        

    print(f"${price:.2f}")