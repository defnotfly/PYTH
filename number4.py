age = int(input("Enter your age: "))
registered = input("Are you registered to vote? (yes/no): ").lower()

if age < 18:
    print("You are too young to vote.")
elif age >= 18 and registered == "yes":
    print("You can vote.")
elif age >= 18 and registered == "no":
    print("You must register before you can vote.")
else:
    print("Invalid input.")