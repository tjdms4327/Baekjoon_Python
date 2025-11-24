import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    h, m, s = map(int, input().strip().split(':'))
    
    bin_h = bin(h)[2:].zfill(6)
    bin_m = bin(m)[2:].zfill(6)
    bin_s = bin(s)[2:].zfill(6)
    
    ans_col = ''
    for i in range(6):
        ans_col += bin_h[i] + bin_m[i] + bin_s[i]
    ans_row = bin_h + bin_m + bin_s
    print(ans_col, ans_row)