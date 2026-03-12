n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
half_coins = sum(coins)/2
s=0
for i in range(n):
    s += coins[i]
    if s>half_coins:
        print(i+1)
        break
