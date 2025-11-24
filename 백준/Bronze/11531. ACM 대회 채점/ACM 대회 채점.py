import sys
input = sys.stdin.readline

wrong_q = {}

penalty = 0
count = 0

while True:
    line = input().strip()
    if line == '-1':
        break
    
    time, q, result = line.split()
    time = int(time)
    if result == 'right':
        count += 1
        penalty += time
        if q in wrong_q:
            penalty += 20*wrong_q[q]
    else: #'wrong'
        if q in wrong_q:
            wrong_q[q] += 1
        else:
            wrong_q[q] = 1

print(count, penalty)