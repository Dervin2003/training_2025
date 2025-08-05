from array import array

# Array from the 'array' module, which can only hold one data type.
# The 'i' is a type code for signed integers. Other examples: 'f' for float, 'd' for double.
my_array = array('i', [10, 20, 30, 40, 50])
print("Array:", my_array)
print("Type of my_array:", type(my_array))

# Looping through an array
print("\nLooping through array:")
for element in my_array:
    print(element)

# Array methods (list methods)
my_array.append(60)
print("Array after append:", my_array)

my_array.insert(1, 15)
print("Array after insert:", my_array)

my_array.remove(30)
print("Array after remove:", my_array)

my_array.pop()
print("Array after pop (removes last element):", my_array)

my_array.pop(0)
print("Array after pop (removes element at index 0):", my_array)

print("Index of 40:", my_array.index(40))

print("Count of 20:", my_array.count(20))

# Note: The 'array.array' object does not have a 'sort' method like lists do.
# To sort it, you would typically convert it to a list, sort, and convert back if needed.

my_array.reverse()
print("Array after reverse:", my_array)

# The 'array.array' object does not have a .copy() method like a list.
# A common and idiomatic way to create a shallow copy is by using a full slice [:].
my_array_copy = my_array[:]
print("Copied array:", my_array_copy) 

# Let's demonstrate the type enforcement by trying to add a string
try:
    my_array.append("hello")
except TypeError as e:
    print(f"\nError when trying to add a non-integer: {e}")

print(type(my_array_copy))

# Note: The 'array.array' object does not have a 'clear' method.
# To clear it, you could reassign it: my_array = array.array('i', [])
print("Length of array:", len(my_array_copy))
