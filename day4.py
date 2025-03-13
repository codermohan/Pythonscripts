#define a function
def greet_user(name):
    return f'Hello {name}!'

#calling function
print(greet_user('Mohan'))

# function multiple parameters
def add_num(a,b):
    return a+b

#calling function
result = add_num(5,6)
print("sum:",result)

#function with default parameter
def power(base, exponent=2):
    return base ** exponent

print("Power of 3:",power(3))
print("Power of 4^4:",power(4,4))
print(power(3,3))
    