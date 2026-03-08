import sys
input = sys.stdin.readline

pattern = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
enharmonic = {
    'B#':'C', 'E#':'F',
    'Cb':'B', 'Fb':'E'
}

while True:
    s = input().strip().split()
    if s == ['***']:  
        break
    
    k = int(input())
    
    result = []
    for x in s:
        if x[-1] == 'b' and x not in enharmonic:
            k_adjust = k - 1
            x = x[:-1]
        else:
            k_adjust = k
        x = enharmonic.get(x, x)
        
        idx = pattern.index(x)
        new_idx = (idx + k_adjust) % 12
        result.append(pattern[new_idx])
    
    print(' '.join(result))