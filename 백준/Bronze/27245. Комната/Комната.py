def check_room(w,l,h):
    if w<l:
        w,l=l,w
    #print(w, l)
    if (l/h>=2) and (w/l<=2):
        return 'good'
    return 'bad'
    
w=float(input())
l=float(input())
h=float(input())

print(check_room(w,l,h))