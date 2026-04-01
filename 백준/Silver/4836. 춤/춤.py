import sys

for line in sys.stdin.read().splitlines():
    words = line.split()
    errors = []
    
    dip_wrong_idx = []
    for i, w in enumerate(words):
        if w == 'dip':
            ok = False
            if i >= 1 and words[i-1] == 'jiggle':
                ok = True
            if i >= 2 and words[i-2] == 'jiggle':
                ok = True
            if i + 1 < len(words) and words[i+1] == 'twirl':
                ok = True
            if not ok:
                dip_wrong_idx.append(i)
    
    if dip_wrong_idx:
        errors.append(1)
    
    if len(words) < 3 or words[-3:] != ['clap', 'stomp', 'clap']:
        errors.append(2)
    
    if 'twirl' in words and 'hop' not in words:
        errors.append(3)
    
    if words and words[0] == 'jiggle':
        errors.append(4)
    
    if 'dip' not in words:
        errors.append(5)
    
    
    
    output_words = words[:]
    if 1 in errors:
        for idx in dip_wrong_idx:
            output_words[idx] = 'DIP'
    
    output_line = ' '.join(output_words)
    if not errors:
        print(f'form ok: {output_line}')
    else:
        errors.sort()
        if len(errors) == 1:
            e = str(errors[0])
            print(f'form error {e}: {output_line}')
        else:
            e = ', '.join(map(str, errors[:-1])) + f' and {errors[-1]}'
            print(f'form errors {e}: {output_line}')