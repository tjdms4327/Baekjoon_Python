# silverIV_4659
import sys
input = sys.stdin.readline

vowels = set('aeiou')

while True:  
    s = input().strip()
    if s == 'end':
        break
    
    has_vowel = any(ch in vowels for ch in s)
    
    sequence_consonant = 0
    sequence_vowel = 0
    prev = ''
    ok = has_vowel
    for ch in s:
        if ch in vowels:
            sequence_vowel += 1
            sequence_consonant = 0
        else:
            sequence_consonant += 1
            sequence_vowel = 0
        if sequence_consonant >= 3 or sequence_vowel >= 3:
            ok = False
            break
        
        if (prev == ch) and (ch not in 'eo'):
            ok = False
            break
        prev = ch
    
    if ok:
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')