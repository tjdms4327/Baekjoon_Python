n=int(input())
st=input()

s=st.count('s')
t=st.count('t')
while s!=t:
    st=st[1:]
    s=st.count('s')
    t=st.count('t')
print(st)