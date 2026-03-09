n=int(input())
m=list(map(int,input().split()))
a=[]
b=[]
c=m[0]%2
for i in m:
    if i%2 == c:
        a.append(i)
    else:
        b.append(i)
if len(a)==1:
    print(m.index(a[0])+1)
else:
    print(m.index(b[0])+1)
