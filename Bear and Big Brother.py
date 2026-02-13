l,b=list(map(int,input().split()))
n=0
while(l<=b):
    n+=1
    l*=3
    b*=2
print(n)
