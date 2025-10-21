# bronzeI_2596
import sys
input = sys.stdin.readline

mapping = {'000000':'A', '001111':'B', '010011':'C', '011100':'D',
           '100110':'E', '101001':'F', '110101':'G', '111010':'H'}

n = int(input())
s = input().strip()

result = ''
for i in range(0, n*6, 6):
    slice = s[i:i+6]
    if slice in mapping:
        result += mapping[slice]
    else:
        found = False
        for ch, alphabet in mapping.items():
            diff_count = sum(1 for x, y in zip(slice, ch) if x != y)
            if diff_count == 1:
                result += alphabet
                found = True
                break
        if not found:
            print(i//6 + 1)
            sys.exit()
print(result)