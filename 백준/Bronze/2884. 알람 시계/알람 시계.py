H,M=input().split()
H=int(H)
M=int(M)

if M>=45:
    M=M-45
    print(H,M)
else:
    if H==0:
        H=23
    else:
        H=H-1
    M=M+15
    print(H,M)