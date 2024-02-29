#CONDITIONAL STATEMENTS

#Write a python program that takes the age of a user as input and categorizes  them into one of three age groups: child, adult, and senior 

# Take the users age as input
age = int(input("Enter your age: "))

# Determine the age group

if age < 18:
    print(f"You are {age} years old. You are a child.")
elif age >= 18 and age < 65:
    print(f"You are {age} years old. You are an adult.")
else:
    print(f"You are {age} years old. You are a senior.")

# Create a simple calculator that takes two numbers and an operator (+, -, *, /) as input and performs the corresponding calculation
    
# Take the user input 

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /)")

if operator == "+":
    print(f"The result is: {num1 + num2}")
elif operator == "-":
    print(f"The result is: {num1 - num2}")
elif operator == "*":
    print(f"The result is: {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"The result is: {num1 / num2}")
    else:
        print(f"Canot divide by zero.")
else: 
    print("Invalid operator.")


# Write a Python program that first asks the user if they are a vegetarian. If yes, ask if they eat eggs. Display appropriate meal choices based on their answers.
    
name = input("Name: ")
print("Hello, " + name)
