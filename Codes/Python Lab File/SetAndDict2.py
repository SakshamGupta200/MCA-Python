my_set = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}

# Find the maximum value in the set
max_value = max(my_set)
print("Maximum value:", max_value)

# Find the minimum value in the set
min_value = min(my_set)
print("Minimum value:", min_value)


def count_vowels(input_string):
    vowels = set("aeiouAEIOU")
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count


# Example usage
input_string = "Hello, World!"
result = count_vowels(input_string)

print("Number of vowels in the given string:", result)

# Dictionary with keys as tuples
multikey_dict = {('John', 'Doe'): 25, ('Jane', 'Smith'): 30, ('Bob', 'Johnson'): 22}

# Accessing values using keys
print("Age of John Doe:", multikey_dict[('John', 'Doe')])

# Adding a new entry
multikey_dict[('Alice', 'Jones')] = 28

# Displaying the updated dictionary
print("Updated Dictionary:", multikey_dict)

my_dict = {'apple': 10, 'banana': 5, 'orange': 8, 'grape': 3}

# Calculate the sum of all values in the dictionary
total_sum = sum(my_dict.values())

print("Sum of all items in the dictionary:", total_sum)
