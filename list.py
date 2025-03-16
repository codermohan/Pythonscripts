#creating a list
squared_numbers = []
for num in range(1,6):
    squared_numbers.append(num**2)
print("Squared Numbers Loop:",squared_numbers)


#list comprehension for the above way

squared_numbers_comprehension = [num**2 for num in range(1,6)]
print("Squared number comprehension:",squared_numbers_comprehension)