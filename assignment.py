
filename = input("Enter the filename: ")

try:
    # Try opening the file for reading
    with open(filename, "r") as f:
        data = f.read()

    # Make it uppercase
    new_data = data.upper()

    # Write to a new file
    with open("output.txt", "w") as f:
        f.write(new_data)

    print("File modified and saved as output.txt")

except FileNotFoundError:
    print("Error: File not found.")
except:
    print("Error: Could not read the file.")
