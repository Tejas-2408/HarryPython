
## positional arguments
def add(a,b):
    return a+b 

c = add(3,5)
print(c)


## Default arguments
def add2(a,b,c=0):
    return a+b+c 

print(add2(2,3))
print(add2(1,2,3))


## Keyword Arguments
x = add(b=5,a=3)
print(x)