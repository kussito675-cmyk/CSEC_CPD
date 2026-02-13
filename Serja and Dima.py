n=int(input())
Serja=0
Dima=0
game=list(map(int,input().split()))
for i in range(n):
    Dima_taked=True
    if len(game)==0:
        break
    if game[0]>game[-1]:
        Serja+=game.pop(0)
        if len(game)>0:
            if game[0]>game[-1]:
                Dima+=game.pop(0)
                Dima_taked=False
            else:
                Dima+=game.pop()
                Dima_taked=False
    else:
        Serja+=game.pop()
        if len(game)>0:
            if Dima_taked:
                if game[0]>game[-1]:
                    Dima+=game.pop(0)
                else:
                    Dima+=game.pop() 
print(Serja,Dima)
