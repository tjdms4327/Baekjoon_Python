import sys
input = sys.stdin.readline

month_mapping = {
    'January':31, 'February':28, 'March':31, 
    'April':30, 'May':31, 'June':30, 
    'July':31, 'August':31, 'September':30,
    'October':31, 'November':30, 'December':31}

tot_day = 365

line = list(input().strip().split())
Month, D, Y, time = line
D, Y = int(D[:-1]), int(Y)
h, m = map(int, time.split(':'))

if (Y%400==0) or (Y%4==0 and Y%100!=0):
    month_mapping['February'] = 29

tot = sum(month_mapping.values())*24*60
    
pass_days = 0
for month, month_d in month_mapping.items():
    if Month == month:
        pass_days += D-1
        break
    else: 
        pass_days += month_d

pass_time = pass_days*24*60 + 60*h + m
print(100 * pass_time / tot)
