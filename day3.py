age = int(input("Enter your age: "))
if age<18:
    print("You are a minor")
elif age<60:
    print("You are a adult.")
else:
    print("You are a Senior Citizen")


#Checking if a number is even or odd
number = int(input("Enter a number:"))

if number % 2 == 0:
    print(number ,"is an even number ")

else:
    print(number ,"is odd number") 