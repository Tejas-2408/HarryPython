def sum(a,b):
    return a+b 

def sum(*args):
    print(args)
    total= 0
    for i in args:
        total+=i 
    return total

print(sum(1,2,3))
print(sum(2,3,4,5,6))


def marks(**kwargs):
    for item in kwargs.keys():
        print(kwargs[item])


marks(tejas=23,ravi=25,ram=30)