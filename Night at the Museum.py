name=input()
alpha="nopqrstuvwxyzabcdefghijklm"
pointer='a'
total=0
for chr in name:
    x,y=0,0
    p=alpha.index(pointer)
    x=alpha[p:]+alpha[:p]
    y=alpha[p:]+alpha[:p]
    s1=len(x[:x.index(chr)])       
    s2=len(y[y.index(chr):])
    pointer=chr
    if s1>s2:
        total+=s2
    else:
        total+=s1
print(total)
