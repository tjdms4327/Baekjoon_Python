import sys
input = sys.stdin.readline

troom, tcond = map(int, input().split())
action = input().strip()

if action == 'fan': print(troom)
elif action == 'auto': print(tcond)
elif action == 'freeze':
    print(min(troom, tcond))
elif action == 'heat':
    print(max(troom, tcond))