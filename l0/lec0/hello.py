# Ask user for their name
# name = input("What's your name? ")

# Remove whitespace from str
# name = name.strip()

# # Capitalize user's name
# # name = name.capitalize()
# name = name.title()

# Remove whitespace from str and capitalize user's name
# name = name.strip().title()

# Ask user for their name
name = input("What's your name? ").strip().title()

# Say hello to user
# print("hello, " + name)
# print("hello,", name)
# print("hello, ", end="")
# print(name)
print(f"hello, {name}")