m = input()
if (len(m)-(m.count('4')+m.count('7')) != 0) and ((int(m)%4 == 0 or (int(m)%7 == 0) or int(m)%47 ==0 or int(m)%74 == 0) ):
    print("YES")
elif len(m)-(m.count('4')+m.count('7')) == 0:
    print("YES")
else:
    print("NO")
