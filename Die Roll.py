Y, W =map(int, input().split())
M = max(Y, W)
fav = 7 - M
total = 6
if fav <= 0:
    print("0/1")
else:
    a, b = fav, total
    while b:
        a, b = b, a % b
    gcd = a
    print(f"{fav // gcd}/{total // gcd}")
