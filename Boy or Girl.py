a=input().upper()
b=[]
n=0
for chr in a:
    if chr not in b:
        b.append(chr)
        n+=1
if n%2!=0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
