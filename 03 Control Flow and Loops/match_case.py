a = int(input("Guess the number: "))

match a:
    case 122:
        print("The value is 122")
    case 3:
        print("The value is 3")
    case 23:
        print("The value is 23")
    case _:
        print("Better luck next time")