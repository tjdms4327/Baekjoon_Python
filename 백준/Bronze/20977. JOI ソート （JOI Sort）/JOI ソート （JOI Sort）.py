order = {'J': 0, 'O': 1, 'I': 2}

n = int(input())
s = input().strip()

print(''.join(sorted(s, key=lambda x:order[x])))