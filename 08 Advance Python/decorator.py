# def decorator(func):
#     def wrapper():
#         print("I am about to execute a function....")
#         func()
#         print("I have executed this function....")
#     return wrapper

# @decorator
# def say_hello():
#     print("hello")


# # say_hello()

# f = decorator(say_hello)
# f()

# say_hello()


## Decorators with Arguments
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def say_hello(a):
    print(f"hello {a}")


say_hello("tejas")