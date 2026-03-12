n, b = list(map(int, input().split()))
if n%2 != 0:
    n+=1
if b<=n//2:
    print(2*b-1)
else:
    print(2*(b-(n//2)))
