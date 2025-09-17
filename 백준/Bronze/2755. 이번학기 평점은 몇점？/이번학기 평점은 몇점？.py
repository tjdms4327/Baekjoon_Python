import sys
input = sys.stdin.readline

n = int(input())
subject = [list(input().strip().split()) for _ in range(n)]


tot, time = 0, 0
mapping = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D0': 1.0, 'D-': 0.7, 'F': 0.0}
for s in subject:
    time += int(s[1])
    tot += mapping[s[2]] * int(s[1])

print('%.2f' % (round(tot/time+10**(-10), 2)))