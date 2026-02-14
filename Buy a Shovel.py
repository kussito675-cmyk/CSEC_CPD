a,b=list(map(int,input().split()))
shovel=0
while True:
    shovel+=1
    if (a*shovel-b)%10 ==0 or a*shovel%10==0 :
        break
print(shovel)
