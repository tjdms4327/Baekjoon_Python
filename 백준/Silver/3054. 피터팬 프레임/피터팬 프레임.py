import sys
input = sys.stdin.readline

def peter(x):
    return ['.#.#.', '#.'+x+'.#', '.#.#.', '..#..']

def wendy(x):
    return ['..*..', '.*.*.', '*.'+x+'.*', '.*.*.', '..*..']


s = input().strip()
length = len(s)

result = ['..#..']
for i in range(1, 1+length):
    x = s[i-1]
    if i% 3 == 0:
        result.pop()
        result.extend(wendy(x))
    else:
        result.extend(peter(x))
        
                
for col in zip(*result):
    print(''.join(col))