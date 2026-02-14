n=int(input())
games=[]
cout=0
for i in range(n):
    game=list(map(int,input().split()))
    games.append(game)
for i in range(n):
    for j in range(n):
        if games[i][0]==games[j][1]:
            cout+=1
print(cout)
