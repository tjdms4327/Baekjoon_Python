import sys
input = sys.stdin.readline

s = list(input().strip())
stack = []

for x in s:
    if x in '([':
        stack.append(x)
    elif x == ')':
        tmp = 0
        while stack:
            top = stack.pop()
            if top == '(':
                stack.append(2 if tmp == 0 else 2*tmp)
                break
            elif isinstance(top, int):
                tmp += top
            else:
                print(0)
                sys.exit()
        else:  # '(' 못 찾았을 때
            print(0)
            sys.exit()
    elif x == ']':
        tmp = 0
        while stack:
            top = stack.pop()
            if top == '[':
                stack.append(3 if tmp == 0 else 3*tmp)
                break
            elif isinstance(top, int):
                tmp += top
            else:
                print(0)
                sys.exit()
        else:  # '[' 못 찾았을 때
            print(0)
            sys.exit()
    else:
        print(0)
        sys.exit()


result = 0
for x in stack:
    if isinstance(x, int):
        result += x
    else:
        print(0)
        sys.exit()

print(result)