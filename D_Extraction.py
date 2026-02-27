n=int(input())
for i in range(n):
    a=str(input())
    print(len(a)-a.count('0'))
    if len(a)>1:
        for i,chr in enumerate(a):
            if int(chr)>0:
                b=(int(chr)*10**(len(a[i:])-1))
                print(b,end=' ')
        print()
    else:print(a)