# Create an empty list
my_list = []

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at index 1
my_list.insert(1, 15)  

# extending a list
my_list.extend([50, 60, 70])

# remove the last element
my_list.pop()

# sort in ascending order
my_list.sort() 

# find and print the index of 30 
index= my_list.index(30)
print(index)