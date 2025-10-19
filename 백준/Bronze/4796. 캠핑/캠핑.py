# bronzeI_4796
import sys
input = sys.stdin.readline

case = 0
while True:  
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    
    case += 1
    use = v//p * l + min(v%p, l)
    print(f'Case {case}: {use}')