import sys
input = sys.stdin.readline

n = int(input())
s = input().strip().lower()
new = input().strip().lower()

if s == new:
    print('Good')
else:
    water_before = s.count('w')
    water_after = new.count('w')
    if water_before == water_after:
        print('Its fine')
    elif water_before > water_after:
        print('Oryang')
    else:
        print('Manners maketh man')