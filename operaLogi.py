x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)    
print(not(z))

print("*****************\n")

x = 4
y = 1

a = x & y
b = x | y
c = ~ x
d = x ^ 5
e = x >> 2
f = x << 2

print("a= ",a,"\nb= ",b,"\nc= ",c,"\nd= ",d,"\ne= ",e,"\nf= ",f) 