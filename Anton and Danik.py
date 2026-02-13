n=int(input())
row=input()
if row.count('A')>row.count('D'):
    print("Anton")
elif row.count('A')<row.count('D'):
    print("Danik")
else:
    print("Friendship")
