n=int(input())
string=input()
temp=""
x=0
for i,chr in enumerate(string):
    if temp != chr:
        if len(string) < n-1:
            if chr != string[i+1]:
                temp=chr
                x += 1
        else:
            if temp != chr:
                temp=chr
                x +=1
print(n-x)
