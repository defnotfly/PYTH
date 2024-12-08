# Define ko dito ung mga functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."


print("Python Calculator \n")
#choices toh pre
x, y = map(float, input("Enter the first and second number separated by space: ").split())
choice = input(
    "MENU \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit \n\n Choose a number from 1-5. \n")
    
if choice == '1':
    print(f"{x} + {y} is equals to {x + y}")

elif choice == '2':
    print(f"{x} - {y} is equals to {x - y}")

elif choice == '3':
    print(f"{x} * {y} is equals to {x * y}")

elif choice == '4':
    print(f"{x} / {y} is equals to {x / y}")

else:
    print("Invalid input")


