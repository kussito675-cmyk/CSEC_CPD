m=list(list(map(int,input().split())) for i in range(5))
s=0
for i,r in enumerate(m):
    if 1 in r and r!=m[2]:
        a=m.pop(2)
        m.insert(2,r)
        m.pop(i)
        m.insert(i,a)
        if i<2:
            s+=(len(m[i:2]))
            break
        s+=len(m[2:i])
for i,v in enumerate(m[2]):
    if v==1 and m[2][2]!=1:
        b=m[2].pop(2)
        m[2].insert(2,v)
        m[2].pop(i)
        m[2].insert(i,b)
        if i<2:
            s+=len(m[2][i:2])
            break
        s+=len(m[2][2:i])
print(s)