try:
    filename = input("Enter file name to read: ")
    # Try to open and read the file
    file = open(filename, 'r') 
    content = file.read()
    
    # Modify the content 
    modified = "Hello Friend,\n" + content
    
    # Write to a new file
    
    new_file = open("new" + filename, 'w')
    new_file.write(modified)
    
    print("File was read and modified successfully!")

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f" An error occurred: {e}")
finally:
    print("Thank you for trying exception handling")
   
