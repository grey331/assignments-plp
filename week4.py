try:
    # Try to open and read the file
    file = open("grey.txt", 'r') 
    content = file.read()
    
    # Modify the content (example: add a line at the top)
    modified = "Hello Friend,\n" + content
    
    # Write to a new file
    # with open("newgrey.txt", 'w')as new_file:

    new_file = open("newgrey.txt", 'w')
    new_file.write(modified)
    
    print("File was read and modified successfully!")

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f" An error occurred: {e}")
finally:
    print("Thank you for trying exception handling")
   
