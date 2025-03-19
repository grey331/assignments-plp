#calculator
no1=float(input("enter the first number: "))
no2=float(input("enter the  second number: "))
operation = input("Choose an operation (+, -, *, /): ")
#operations
if operation == "+":
    #display results
    print(f"{no1} {operation} {no2} = {no1+no2}")
elif operation =="-":
    #display results
    print(f"{no1} {operation} {no2} = {no1-no2}")
elif operation=="*":
    #display results
    print(f"{no1} {operation} {no2} = {no1*no2}")
elif operation=="/":
    if no2 == 0:
        print("division error")
    else:
        #display results
        print(f"{no1} {operation} {no2} = {no1/no2}")
else:
    print("kindly choose an applicable operator")
    

