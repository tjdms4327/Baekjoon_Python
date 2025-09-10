import sys
input = sys.stdin.readline

n = int(input())
me = list(input().strip())
guile = list(input().strip())

def me_win(i):
    global win, lose
    if me[i] == guile[i]:
        pass
    elif me[i] == 'R' and guile[i] == 'S':
        win += 1
    elif me[i] == 'S' and guile[i] == 'P':
        win += 1
    elif me[i] == 'P' and guile[i] == 'R':
        win += 1
    else:
        lose += 1
    return 0

win, lose = 0, 0
for i in range(n):
    me_win(i)
if win > lose:
    print('victory')
else: print('defeat')