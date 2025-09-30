# Writing to a file
with open("C:/Users/Ascendion/Desktop/test_upload.txt", "w") as file:
    file.write("Hello, File World!\n")
    file.write("This is a second line.\n")
    file.write("Python is awesome!\n")

print("File written successfully!")

# Reading from a file
print("\nReading file content:")
with open("C:/Users/Ascendion/Desktop/test_upload.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
print("Reading line by line:")
with open("C:/Users/Ascendion/Desktop/test_upload.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")

# Appending to a file
with open("C:/Users/Ascendion/Desktop/test_upload.txt", "a") as file:
    file.write("This line was appended later.\n")

print("\nFile after appending:")
with open("C:/Users/Ascendion/Desktop/test_upload.txt", "r") as file:
    print(file.read())
