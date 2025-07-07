import sys
input=sys.stdin.readline

while True:
    # x=sweet, y=sour jars
    x, y=map(int, input().strip().split())
    if x+y==0: break # 0 <= x, y <= 1000

    if x+y==13: print("Never speak again.")
    elif x<y: print("Left beehind.")
    elif x>y: print("To the convention.")
    else: print("Undecided.")