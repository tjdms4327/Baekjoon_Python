import sys
input=sys.stdin.readline

s=input().strip()
if 'A' in s:
    for c in 'BCDF':
        s = s.translate(str.maketrans({c: 'A' for c in 'BCDF'}))
elif 'B' in s:
        s = s.translate(str.maketrans({c: 'B' for c in 'CDF'}))
elif 'C' in s:
        s = s.translate(str.maketrans({c: 'C' for c in 'DF'}))
else:
    s='A'*len(s)
print(s)