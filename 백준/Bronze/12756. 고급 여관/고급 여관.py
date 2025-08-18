import sys
input = sys.stdin.readline

a_attack, a_life = map(int, input().split())
b_attack, b_life = map(int, input().split())



while a_life > 0 and b_life > 0:
    a_life -= b_attack
    b_life -= a_attack

if  a_life <= 0 and b_life <= 0:
    print('DRAW')
elif a_life <= 0:
    print("PLAYER B")
else:
    print("PLAYER A")