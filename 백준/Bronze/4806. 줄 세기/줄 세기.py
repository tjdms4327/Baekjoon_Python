cnt=0
while True:
    try:
        input()
        cnt+=1
    except EOFError:
        break
print(cnt)