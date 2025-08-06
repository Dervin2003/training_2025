import os
# Basic File Handling

# Writing to a file
# try:
#     with open("my_file.txt", "w") as file:
#         file.write("Hello, this is a test file.\n")
#         file.write("This is the second line.\n")
#     print("Successfully wrote to my_file.txt")
# except IOError as e:
#     print(f"Error writing to file: {e}")


file1 = open("my_file1.txt", "r")
content = file1.read()
print(content)

# file1 = open("my_file1.txt", "w")
# file1.write("vbkuhbhjub")

# file1 = open("my_file1.txt", "u")
# content = file1.read()
# print(content)



# Reading from a file
# try:
#     with open("my_file.txt", "r") as file:
#         content = file.read()
#         print("\nContent of my_file.txt:")
#         print(content)
# except FileNotFoundError:
#     print("Error: my_file.txt not found.")
# except IOError as e:
#     print(f"Error reading from file: {e}")

# # Appending to a file
# try:
#     with open("my_file.txt", "a") as file:
#         file.write("This line was appended.\n")
#     print("Successfully appended to my_file.txt")
# except IOError as e:
#     print(f"Error appending to file: {e}")

# # Reading line by line
# try:
#     with open("my_file.txt", "r") as file:
#         print("\nContent of my_file.txt (line by line):")
#         for line in file:
#             print(line.strip()) # .strip() removes leading/trailing whitespace, including newline characters
# except FileNotFoundError:
#     print("Error: my_file.txt not found.")
# except IOError as e:
#     print(f"Error reading from file: {e}")

# # Using readlines()
# try:
#     with open("my_file.txt", "r") as file:
#         lines = file.readlines()
#         print("\nContent of my_file.txt (using readlines()):")
#         for line in lines:
#             print(line.strip())
# except FileNotFoundError:
#     print("Error: my_file.txt not found.")
# except IOError as e:
#     print(f"Error reading from file: {e}")

# # Exclusive creation ('x' mode) - creates a file, but fails if it exists
# try:
#     # This will create 'new_file.txt'. If you run the script again, it will fail.
#     with open("new_file.txt", "x") as file:
#         file.write("This file was created exclusively.\n")
#     print("\nSuccessfully created new_file.txt")
# except FileExistsError:
#     print("\nError: new_file.txt already exists. Delete the file to run this part again.")
# except IOError as e:
#     print(f"Error creating file: {e}")

# # Clean up the created files
# if os.path.exists("my_file.txt"):
#     os.remove("my_file.txt")
#     print("\nCleaned up my_file.txt")

abc = os.path.abspath("my_file.txt")
print(abc)

print(os.path.abspath(abc))

