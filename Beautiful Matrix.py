m=list(list(map(int,input().split())) for i in range(5))
s=0
for r in m:
    if 1 in r:
        i=m.index(r)
        j=r.index(1)
        s=(len(m[i:2])+len(m[2:i])+len(r[j:2])+len(r[2:j]))
print(s) 
