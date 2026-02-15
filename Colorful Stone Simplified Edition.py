rocks=input()
rock_color=input()
x=0
y=1
for color in rock_color:
    if color==rocks[x]:
        y+=1
        x+=1
print(y)
