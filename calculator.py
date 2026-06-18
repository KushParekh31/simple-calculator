# Function to add two numbers
def addition(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def subtraction(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiplication(num1, num2):
    return num1 * num2


# Function to divide two numbers
def division(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero!"
    return num1 / num2


# Function to find power
def power(num1, num2):
    return num1 ** num2


# Function to find modulus
def modulus(num1, num2):
    if num2 == 0:
        return "Cannot perform modulus by zero!"
    return num1 % num2


# Function for floor division
def floor_division(num1, num2):
    if num2 == 0:
        return "Cannot perform floor division by zero!"
    return num1 // num2


# Store calculation history
history = []

# Dictionary of operations
operations = {
    1: ("+", addition),
    2: ("-", subtraction),
    3: ("*", multiplication),
    4: ("/", division),
    5: ("**", power),
    6: ("%", modulus),
    7: ("//", floor_division)
}

print("*" * 35)
print("\tCalculator")
print("*" * 35)

while True:

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Floor Division")
    print("8. View History")
    print("9. Exit")

    try:
        choice = int(input("\nEnter your choice (1-9): "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choice == 9:
        print("\nThanks for using the calculator!")
        break

    if choice == 8:
        print("\n===== Calculation History =====")
        if not history:
            print("No calculations performed yet.")
        else:
            for item in history:
                print(item)
        continue

    if choice not in operations:
        print("Invalid choice!")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers!")
        continue

    symbol, operation = operations[choice]
    result = operation(num1, num2)

    expression = f"{num1} {symbol} {num2} = {result}"

    print("\nResult:")
    print(expression)

    history.append(expression)

    again = input("\nDo another calculation? (y/n): ").lower()

    if again != "y":
        print("\nThanks for using the calculator!")
        break
