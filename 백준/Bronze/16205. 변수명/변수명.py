# bronzeI_16205
import re

n, s = input().split()

if n == '1':  # camelCase
    camel = s
    snake = re.sub('([A-Z])', lambda x: '_' + x.group(1).lower(), s)
    pascal = s[0].upper() + s[1:]

elif n == '2':  # snake_case
    parts = s.split('_')
    camel = parts[0] + ''.join(p.capitalize() for p in parts[1:])
    snake = s
    pascal = ''.join(p.capitalize() for p in parts)

else:  # PascalCase
    camel = s[0].lower() + s[1:]
    snake = re.sub('([A-Z])', lambda x: '_' + x.group(1).lower(), s).lstrip('_')
    pascal = s

print(camel)
print(snake)
print(pascal)
