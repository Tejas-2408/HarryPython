# while True:
#     try:   
#         a = int(input("Enter a number: "))
#         b = int(input("Enter a number: "))
#         print(f"The sum is {a+b}")
    
#     except Exception as e:
#         print("Some error occurred",e)


# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))

# if b==0:
#     raise ValueError("Don't divide by zero")



# try:
#     a = 23/0
# except Exception as e:
#     print(e)
# else:  ## get executed when there is no error in try block
#     print("hey I am good")


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

try:
    c = a/b 
    print(c)
except Exception as e:
    print(e)
finally:
    print("This will always executed")