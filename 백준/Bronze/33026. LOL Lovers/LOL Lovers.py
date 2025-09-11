import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

for i in range(1, n):
    me_L, me_O = s[:i].count('L'), s[:i].count('O')
    friend_L, friend_O = s[i:].count('L'), s[i:].count('O')

    if me_L != friend_L and me_O != friend_O:
        print(i)
        sys.exit()
else:
    print(-1)