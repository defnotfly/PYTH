first, second = input("Enter two-seperated characters: ").split()

ch1 = ord(first)
ch2 = ord(second)

greaterascii = max(first, second)

print("--------------------")
print(f"The character with greater value is: {greaterascii}")
print("--------------------")
print("This part is optional to include.")
print("Showing ASCIII Values:")
print(f"{first} : {ch1}")
print(f"{second} : {ch2}")