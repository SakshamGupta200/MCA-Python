# Create a list of fruits.
fruits = ['apple', 'banana', 'cherry']
print(fruits)
# Add a new fruit to the list and display the updated list.

fruits.append('mango')
print(fruits)
# Remove one fruit from the list and display the updated list.

fruits.remove('banana')
print(fruits)
# Write a program that searches for a specific element in a list and returns its index.

def search_element(fruits, element):
    for i in range(len(fruits)):
        if fruits[i] == element:
            return i
    return -1

fruit_index = search_element(fruits, 'cherry')

if fruit_index != -1:
    print("Element found at index", fruit_index)
else:
    print("Element not found in the list")
# Explanation of the search algorithm used in the program.
# The search_element function iterates through each element in the list using a for loop.
# Inside the loop, the function checks if the current element is equal to the element being searched for. If it is, the function returns the index of the current element. If the function reaches the end of the list without finding the element, it returns -1, indicating that the element is not present in the list.
#
# The search algorithm used in this program is a linear search algorithm, which has a worst-case time complexity of O(n), where n is the number of elements in the list. In other words, the time it takes to find the element increases linearly with the size of the list. However, since we're dealing with a list of strings (which are mutable and cannot be used as dictionary keys), using a different data structure like a dictionary with the fruit names as keys and their indices as values would provide faster access times.