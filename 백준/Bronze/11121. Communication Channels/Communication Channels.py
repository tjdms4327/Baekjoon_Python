t=int(input())
for _ in range(t):
    input_b, output_b=input().split()
    if input_b==output_b:
        print('OK')
    else:
        print('ERROR')