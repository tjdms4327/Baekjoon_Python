import sys
input = sys.stdin.readline

case = 0
while True:
    n = int(input())
    if n == 0: break
    
    case += 1
    total_chicken = total_beef = total_lamb = total_nasi = 0
    for _ in range(n):
        c, b, l, nasi = map(int, input().split())
        total_chicken += c
        total_beef += b
        total_lamb += l
        total_nasi += nasi

    gross = total_chicken*0.80 + total_beef*1.00 + total_lamb*1.20 + total_nasi*0.80
    
    meat_cost = (total_chicken/85)*7.50 + (total_beef/85)*24.00 + (total_lamb/85)*32.00
    spice_cost = ((total_chicken + total_beef + total_lamb)/85)*8.00
    nasi_cost = total_nasi*0.20
    cost = meat_cost + spice_cost + nasi_cost

    print(f"Case #{case}: RM{gross - cost:.2f}")
