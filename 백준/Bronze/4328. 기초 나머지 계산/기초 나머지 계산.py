import sys
input = sys.stdin.readline

while True:
    line = input().split()
    if len(line) == 1 and line[0] == '0':
        break
    
    b, p, m = line
    b = int(b)
    m_val = int(m, b)
    
    res = 0
    for ch in p:
        digit = int(ch)
        res = (res * b + digit) % m_val
    
    if res == 0:
        print(0)
    else:
        ans = ""
        while res > 0:
            ans = str(res % b) + ans
            res //= b
        print(ans)