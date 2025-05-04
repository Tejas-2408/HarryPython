def very_slow_function():
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    return 8

# if very_slow_function()>10:
#     print(very_slow_function())
# else:
#     print("It is not greater than 10")

# a = very_slow_function()
# if a>10:
#     print(a)
# else:
#     print("It is not greater than 10")

if ((a:=very_slow_function())>10):
    print(a)
else:
    print("It is not greater than 10")