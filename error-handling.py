def read_file_with_error_handling():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content read successfully!")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")

# Example usage
read_file_with_error_handling()
