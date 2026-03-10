word = input().lower()
b = "aoyeui"
c = ['.'+ chr for chr in word if (chr not in b)]
m = ''.join(c)
print(m)
