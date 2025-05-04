from functools import reduce 

n = [1,2,4,5,6,7,8]

def square(x):
    return x*x 

new = map(square,n)
print(new)
print(list(new))

n = [12,234,234,56,78,1,2,3,5]

def is_greater_than_8(x):
    if x>8:
        return True
    else:
        return False
    
f_n = filter(is_greater_than_8,n)
print(f_n)
print(list(f_n))


a = [1,2,3,4,5,6,7]

def sum(a,b):
    return a+b
c = reduce(sum,a)
print(c)
print(type(c))