# Accept a character from the user
char = input("Enter a character: ")

# Convert the character to lowercase or uppercase depending on its case
if char.islower():
    new_char = char.upper()
else:
    new_char = char.lower()

# Print the new character
print("The new character is:", new_char)