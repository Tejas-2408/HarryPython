z = 8  # Global variable can be accessed anywhere

def sum(a,b):
    c = a+b  ## local variable
    z = 1 # It creates a Local variable and won't update the Global variable and will get destroyed after function returns
    return c 


print(sum(4,5))
# print(c) # Throw error as c defined in local of sum function

print(z)


z = 3

def sum1(a,b):
    print("Hey I am summing: ")
    c = a+b
    global z 
    z=0  # This will refer to global variable z
    return c 


print(sum(3,12))
print(z)