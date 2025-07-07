def jay():
    count=0
    while True:
        try:
            gum=input()
            count+=1
        except EOFError:
            break
    return count

print(jay())