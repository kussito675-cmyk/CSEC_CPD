a=list(map(int,input().split()))
b=0
pr=[]
for m in a:
    if a.count(m)>1 and m not in pr:
        pr.append(m)
        b+=a.count(m)-1
print(b)
