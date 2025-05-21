#program to read text file
def read_text_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File contents:\n")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
# Example usage
if __name__ == "__main__":
    filename = input("Enter the path to the text file: ")
    read_text_file(filename)

# program to write text to .txt file using  InputStream
import sys
def write_to_file(filename):
    try:
        with open(filename, 'w') as file:
            print("Enter text to write to the file.")
            print("Press Ctrl+D (Linux/Mac) or Ctrl+Z then Enter (Windows) to finish.\n")

            # Read from standard input until EOF
            for line in sys.stdin:
                file.write(line)

        print(f"\nText successfully written to '{filename}'.")

    except IOError:
        print(f"Error: Could not write to the file '{filename}'.")
# Example usage
if __name__ == "__main__":
    filename = input("Enter the name of the file to write to (e.g., output.txt): ")
    write_to_file(filename)

# program to read a file stream
def read_text_stream(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file as text stream:\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError:
        print(f"Error: Could not read file '{filename}'.")
# Example usage
if __name__ == "__main__":
    filename = input("Enter filename to read: ")
    read_text_stream(filename)

#a program to read a file stream supports random access
def read_random_access(filename):
    try:
        with open(filename, 'r') as file:
            print(f"Opened file: {filename}")
            print(f"Total size: {len(file.read())} characters\n")

            file.seek(0)  # Move back to the beginning
            position = int(input("Enter position to seek (0-based index): "))

            file.seek(position)  # Move file pointer to desired position
            print(f"Reading from position {position}...")

            # Read next 20 characters from that position
            content = file.read(20)
            print(f"\nContent from position {position}:\n{content}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Invalid input. Please enter a valid integer position.")
    except IOError:
        print(f"Error: Could not read from the file '{filename}'.")
# Example usage
if __name__ == "__main__":
    filename = input("Enter the name of the file: ")
    read_random_access(filename)

#a program to read a file a just to a particular index using seek()
def read_from_index(filename, index):
    try:
        with open(filename, 'r') as file:
            file.seek(index)  # Move to the specific character index
            data = file.read(20)  # Read 20 characters from that position
            print(f"\nReading from index {index}:\n{data}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: Please provide a valid index number.")
    except IOError:
        print(f"Error: Could not read from the file '{filename}'.")
# Example usage
if __name__ == "__main__":
    filename = input("Enter the file name: ")
    try:
        index = int(input("Enter the index to seek to: "))
        read_from_index(filename, index)
    except ValueError:
        print("Invalid input. Index must be an integer.")

#a program to check whether a file is having read access and write access permissions
import os

filename = input("Enter the file name: ")

if os.access(filename, os.R_OK):
    print("Read access: Yes")
else:
    print("Read access: No")

if os.access(filename, os.W_OK):
    print("Write access: Yes")
else:
    print("Write access: No")



