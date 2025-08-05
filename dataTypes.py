# # List
# my_list = [1, 2, 3, "apple", "banana"]
# my_clist =my_list.copy()

# print(my_clist)
# print("List:", my_list)
# print("Type of my_list:", type(my_list))

# # Looping through a list
# print("\nLooping through list:")
# for item in my_list:
#     print(item)

# # List methods
# my_list.append("cherry")
# print("List after append:", my_list)
# my_list.remove(2)
# print("List after remove:", my_list)
# print("Length of list:", len(my_list))
# print("Index of 'apple':", my_list.index("apple"))
# my_list.insert(1, "orange")
# print("List after insert:", my_list)
# my_list.pop()
# print("List after pop:", my_list)
# my_list.reverse()
# print("List after reverse:", my_list)
# my_list_copy = my_list.copy()
# print("Copied list:", my_list_copy)
# my_list.clear()
# print("List after clear:", my_list)


# # Tuple
# my_tuple = (10, 20, "cat", "dog")
# print("\nTuple:", my_tuple)
# print("Type of my_tuple:", type(my_tuple))

# # Looping through a tuple
# print("\nLooping through tuple:")
# for item in my_tuple:
#     print(item)

# # Tuple methods (limited as tuples are immutable)
# print("Count of 10 in tuple:", my_tuple.count(10))
# print("Index of 'cat' in tuple:", my_tuple.index("cat"))


# Dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# my_dict["name"]="dervin"
print("\nDictionary:", my_dict)
print("Type of my_dict:", type(my_dict))

# data = {'name': 'Alice', 'age': 25, 'city': 'NYC'}
# key_map = {'name': 'first_name', 'city': 'location'}

# for old_key, new_key in key_map.items():
#     if old_key in data:
#         data[new_key] = data.pop(old_key)

# print(data) 

# Looping through a dictionary
print("\nLooping through dictionary (keys):")
for key in my_dict:
    print(key)

print("\nLooping through dictionary (values):")
for value in my_dict.values():
    print(value)

print("\nLooping through dictionary (items):")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# Dictionary methods
# print("\nDictionary methods:")
# print("Value for 'name':", my_dict.get("name"))
# my_dict["country"] = "USA" # Adding a new item
# print("Dictionary after adding 'country':", my_dict)
# my_dict.update({"age": 31, "city": "San Francisco"})
# print("Dictionary after update:", my_dict)
# popped_value = my_dict.pop("city")
# print("Popped value for 'city':", popped_value)
# print("Dictionary after pop:", my_dict)
# my_dict_copy = my_dict.copy()
# print("Copied dictionary:", my_dict_copy)
# my_dict.clear()
# print("Dictionary after clear:", my_dict)
print(my_dict.popitem())
print("Dictionary after popitem:", my_dict)
print(my_dict.pop('city', 'Not Found'))

# # Set
# # Sets are unordered, unindexed, and do not allow duplicate values.
# print("\n# Set")
# my_set = {"apple", "banana", "cherry"}
# print("Set:", my_set)
# print("Type of my_set:", type(my_set))

# # Adding a duplicate item has no effect
# my_set.add("apple")
# print("Set after adding a duplicate 'apple':", my_set)

# # Looping through a set
# print("\nLooping through set:")
# for item in my_set:
#     print(item)

# # Set methods
# print("\nSet methods:")
# my_set.add("orange")
# print("Set after add 'orange':", my_set)
# my_set.update(["mango", "grapes"])
# print("Set after update:", my_set)
# my_set.remove("banana") # Raises KeyError if item not found
# print("Set after remove 'banana':", my_set)
# my_set.discard("kiwi") # Does not raise an error if item not found
# print("Set after discard 'kiwi' (not in set):", my_set)

# # Set Operations
# print("\nSet Operations:")
# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# print(f"Set A: {set_a}")
# print(f"Set B: {set_b}")

# # Union: all unique elements from both sets
# print("Union of A and B:", set_a | set_b)

# # Intersection: elements that are in both sets
# print("Intersection of A and B:", set_a & set_b)

# # Difference: elements in A but not in B
# print("Difference (A - B):", set_a - set_b)

# # Symmetric Difference: elements in either A or B, but not both
# print("Symmetric Difference of A and B:", set_a ^ set_b)
