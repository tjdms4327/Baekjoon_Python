import sys
input = sys.stdin.readline

def change(a, b, ch):
    x = ord(ch) - ord('A')
    e = (a*x + b) % 26 + ord('A')
    return chr(e)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    s = list(input().strip())
    
    result = [change(a, b, ch) for ch in s]
    print(''.join(result))