# Maximum and Minimum a Set.
# Create a set of numbers
numbers = {1, 5, 8, 3, 6, 9, 2}
# Find the maximum and minimum values in the set
max_num = max(numbers)
min_num = min(numbers)
print("Maximum number in the set:", max_num)
print("Minimum number in the set:", min_num)
# Count number of vowels using sets in a given string.
# Define a string
string = "Hello, World!"
# Convert the string to lowercase and create a set of vowels
vowels = set("aeiou")
string_lower = string.lower()
# Count the number of vowels in the string
vowel_count = sum(letter in vowels for letter in string_lower)
print("Number of vowels in the string:", vowel_count)
# Dictionary with keys having multiple inputs.
# Create a dictionary with keys having multiple inputs
students = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 22, "major": "Mathematics"},
    "Charlie": {"age": 21, "major": "Physics"}
}
# Access the values in the dictionary
for name, info in students.items():
    print(f"{name}'s age is {info['age']} and major is {info['major']}")
# Find the sum of all items in a dictionary.
# Create a dictionary of numbers
numbers = {"a": 1, "b": 2, "c": 3, "d": 4}
# Find the sum of all items in the dictionary
sum_numbers = sum(numbers.values())
print("Sum of all items in the dictionary:", sum_numbers)
