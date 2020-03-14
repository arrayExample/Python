print("Welcome to the Express Lane!")
first_price = float(input("Enter the first price: "))
second_price = float(input("Enter the second price: "))
third_price = float(input("Enter the third price: "))
fourth_price = float(input("Enter the fourth price: "))
final_price = float(input("Enter the final price: "))
subtotal = first_price + second_price + third_price + fourth_price + final_price
print("subtotal:", round(subtotal, 2))
sales_tax = subtotal * .06
print("sales tax:", round(sales_tax, 2))
print("-----------------------")
total = (subtotal + sales_tax)
print ("total:", round(total, 2))
""""
-Test Values-
Welcome to the Express Lane!
Enter the first price: 5.00
Enter the second price: 6.15
Enter the third price: 7.95
Enter the fourth price: 42.99
Enter the final price: 12.70
subtotal: 74.79
sales tax: 4.49
-----------------------
total: 74.85
"""""