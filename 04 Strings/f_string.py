a = "Tejas"
a1 = 10000

b = "Ravi"
b1 = 5000

c = "Ram"
c1 = 1000

template = "Dear {}, congratulations on winning {}$ amount"

s1 = template.format(a,a1)
s2 = template.format(b,b1)
s3 = template.format(c,c1)

print(s1)
print(s2)
print(s3)