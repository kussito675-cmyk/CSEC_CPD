players = input()
count = 0
ans = "NO"
preveous = int(players[0])
for i in players:
    if preveous == int(i):
        count += 1
        if count == 6:
            ans = "YES"
            break
    else:
        count = 0
        preveous = int(i)
print(ans)
