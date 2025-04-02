# creating a function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount=price*discount_percent/100
        final_price=price-discount
        return final_price
    else:
        return price
    
# prompt user input
price=float(input("enter the original price: "))
discount_percent=float(input("enter the percentage discount: "))

# print the final price
print("the final price is: ",calculate_discount(price,discount_percent))
        
