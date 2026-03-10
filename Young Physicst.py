n = int(input())
a, b, c = 0, 0, 0
for i in range(n):
    m = list(map(int, input().split() ))
    a += m[0]
    b += m[1]
    c += m[2]
if a==b==c==0:
    print("YES")
else:
    print("NO")
