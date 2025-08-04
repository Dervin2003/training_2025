import time
 
def encrypt(text, shift):
    print(f"Text: {text}")
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            new_ascii = ord(char) + shift
            if new_ascii > ord('z'):
                new_ascii -= 26
            result += chr(new_ascii)
        elif 'A' <= char <= 'Z':
            new_ascii = ord(char) + shift
            if new_ascii > ord('Z'):
                new_ascii -= 26
            result += chr(new_ascii)
        else:
            result += char 
    return result
 
start = time.perf_counter()
text = encrypt("Hello World", 4)
print("Result:", text)

end = time.perf_counter()

print("Execution time:", end - start, "seconds")