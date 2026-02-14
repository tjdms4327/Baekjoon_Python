import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

result = ''
i = 0
prev = ''

while i < len(s):  
    slice = s[i]
    if i+1 < len(s) and s[i+1] in '+-0':
        slice += s[i+1]
        i += 1
    i += 1
    
    if len(slice) == 1:
        slice += '0'
    
    if slice in ['C0', 'C-', 'C+']:
        result += 'B'
        
    elif slice in ['B0', 'B-']:
        if prev in ['', 'C0', 'C-', 'C+']:
            result += 'D'
        else:
            result += 'B'
            
    elif slice in ['A-', 'B+']:
        if prev in ['', 'B0', 'B-', 'C0', 'C-', 'C+']:
            result += 'P'
        else:
            result += 'D'
            
    elif slice == 'A0':
        if prev in ['', 'A-', 'B+', 'B0', 'B-', 'C0', 'C-', 'C+']:
            result += 'E'
        else:
            result += 'P'
            
    elif slice == 'A+':
        result += 'E'
        
    prev = slice
    
print(result)
