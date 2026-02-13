a,b=list(map(int,input().split()))
r=list(map(int,input().split()))
w=0
for i in range(a):
    if r[i]>b:
        w+=2
    else:
        w+=1
print(w)
