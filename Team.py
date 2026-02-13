n=int(input())
m=list(list(map(int,input().split())) for i in range(n))
a=0
for r in m:
    if r.count(1)>r.count(0):
        a+=1
print(a)
