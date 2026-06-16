# Function to add two numbers
def addition(num1, num2):
    print(num1 + num2)


# Function to subtract two numbers
def subtraction(num1, num2):
    print(num1 - num2)


# Function to multiply two numbers
def multiplication(num1, num2):
    print(num1 * num2)


# Function to divide two numbers
def division(num1, num2):
    print(num1 / num2)


# Display calculator heading
print("*" * 30)
print("\tCalculator")
print("*" * 30, "\n")

# Display available operations
print("Choose what you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get user's choice
choice = int(input("\nChoose from 1-4: "))

# Validate choice
if choice > 4:
    print("Invalid input!")
else:
    # Get numbers from the user
    num1 = int(input("Enter value of first number: "))
    num2 = int(input("Enter value of second number: "))

    # Perform the selected operation
    match choice:
        case 1:
            addition(num1, num2)
        case 2:
            subtraction(num1, num2)
        case 3:
            multiplication(num1, num2)
        case 4:
            division(num1, num2)

# Display closing message
print("\nThanks for using!")
