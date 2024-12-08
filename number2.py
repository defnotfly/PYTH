name = input("Enter your name: ")

uppercase_name = name.upper()
lowercase_name = name.lower()
title_name = name.title()
name_length = len(name)
reversed_name = name[::-1]
modified_name = name.replace("a", "@").replace("e", "3")
modified_name = name.replace("a", "@").replace("e", "3")


print(f"\nHello, {title_name}!")
print(f"Your name in uppercase: {uppercase_name}")
print(f"Your name in lowercase: {lowercase_name}")
print(f"The length of your name is: {name_length} characters")
print(f"Your name reversed is: {reversed_name}")
print(f"Your name with replacements: {modified_name}")