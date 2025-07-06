n, b = map(int, input().split())

def cal(x, y):
    base = ''
    while x > 0:
        x, mod = divmod(x, y)
        
        if mod < 10:
            base += str(mod)
        else:
            base += chr(ord('A') + mod - 10)
    return base[::-1]

print(cal(n, b))