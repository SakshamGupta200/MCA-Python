# the list of my favorite fruits:
favorite_fruits = ['apple', 'banana', 'orange', 'kiwi', 'grape']
print("Original List of Favorite Fruits:", favorite_fruits)

# add a new fruit to the list:
favorite_fruits.append('pineapple')
print("Updated List after adding 'pineapple':", favorite_fruits)

# remove one fruit from the list:
fruit_to_remove = 'kiwi'
favorite_fruits.remove(fruit_to_remove)
print(f"Updated List after removing '{fruit_to_remove}':", favorite_fruits)

# search for a specific element in a list and returns its index:
def search_element_index(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1

search_element = 'orange'
index = search_element_index(favorite_fruits, search_element)

if index != -1:
    print(f"The index of '{search_element}' is:", index)
else:
    print(f"'{search_element}' not found in the list.")

