import sys
input = sys.stdin.readline

def win(a, b):
    return (a=='S' and b=='P') or (a=='R' and b=='S') or (a=='P' and b=='R')

ML, MR, TL, TR = input().split()

if (win(ML, TL) and win(ML, TR)) or (win(MR, TL) and win(MR, TR)):
    print("MS")
elif (win(TL, ML) and win(TL, MR)) or (win(TR, ML) and win(TR, MR)):
    print("TK")
else:
    print("?")
