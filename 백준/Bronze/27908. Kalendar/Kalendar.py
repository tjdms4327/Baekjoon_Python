import sys
input = sys.stdin.readline

days, start = map(int, input().split())
print('+---------------------+')

weeks = []
cur_week = []
for _ in range(start-1):
    cur_week.append('...')
for day in range(1, days+1):
    if day < 10:
        s = '..' + str(day)
    else:
        s = '.' + str(day)
    cur_week.append(s)
    if len(cur_week) == 7:
        weeks.append('|'+''.join(cur_week)+'|')
        cur_week = []
if cur_week:
    cur_week.extend(['...'] * (7 - len(cur_week)))
    weeks.append('|' + ''.join(cur_week) + '|')

for i in weeks:
    print(i)
print('+---------------------+')