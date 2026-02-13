n=int(input())
mg=0
num_group=0
for i in range(n):
  mag=int(input())
  if mg!=mag:
    mg=mag
    num_group+=1
print(num_group)
