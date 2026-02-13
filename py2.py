item_name = input("Enter the name of the item:")
price = float(input("Enter the price:"))
quan = int(input("Enter the required quantity:")) 
total = price*quan
tax = total*.07
grand_total = total + tax
print(f"----Receipt---")
print(f"The total value of {item_name} is {grand_total}")