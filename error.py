#error handling try and except

try:
    num=int(input("Enter a number:"))
    result = 10/num
    print("Result", result)
except ZeroDivisionError:
    print("Error: Cannot divided by Zero!")
except ValueError:
    print("Error: Enter valid number")


