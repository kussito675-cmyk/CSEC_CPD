a=input()
small=""
captal=""
for chr in a:
    if chr.islower():
        small+=chr
    else:
        captal+=chr
if len(captal)>len(small):
    print(a.upper())
else:
    print(a.lower())
