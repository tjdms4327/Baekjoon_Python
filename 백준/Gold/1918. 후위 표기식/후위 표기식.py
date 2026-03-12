import sys
input = sys.stdin.readline

s = input().strip()

priority = {
    '+':1,
    '-':1,
    '*':2,
    '/':2
}

output = []
stack = []
for ch in s:
    if 'A'<=ch<='Z':
        output.append(ch)
        
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        while True:
            out = stack.pop()
            if out == '(':
                break
            else:
                output.append(out)
                
    else: # 연산자
        while stack and stack[-1]!='(' and priority[stack[-1]] >=priority[ch]:
            output.append(stack.pop())
        stack.append(ch)
        
        
while stack:
    output.append(stack.pop())
    
print(''.join(output))