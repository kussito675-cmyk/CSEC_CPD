n,b = list(map(int,input().split()))
line = list(map(int,input().split()))
row = []
for i in line:
    if i>= line[b-1] and line[b-1] != 0:
        row.append(i)
    elif line[b-1] == 0 and i > 0:
        row.append(i)
print(len(row))
