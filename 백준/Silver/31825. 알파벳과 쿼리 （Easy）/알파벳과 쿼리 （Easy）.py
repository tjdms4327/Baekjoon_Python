import sys
input = sys.stdin.readline

n, q = map(int, input().split())
s = list(input().strip())
for _ in range(q):
    t, l, r = map(int, input().split())
    l -= 1
    r -= 1
    
    if t == 1:
        cnt = 1
        for i in range(l+1, r+1):
            if s[i] != s[i-1]:
                cnt += 1
        print(cnt)
        
    elif t == 2:
        for i in range(l, r+1):
            s[i] = chr((ord(s[i]) - ord('A') + 1) % 26 + ord('A'))