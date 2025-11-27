# Copyright (c) 2025 Simona Schnitzer
# Licensed under the MIT License. See LICENSE file for details.
# -----INVENTORY UPDATE-----
# This script displays all open orders with numbers, asks the user to enter the an order ID to remove, 
# checks if the entered ID matches any existing order (ignoring case, underscores can be replace by space) 
# and if found removes it from the list and confirms, otherwise, it shows "Order not fournd". 

open_orders =["Order_1", "Order_2", "Order_3", "Order_4", "Order_5"]

print("Open orders")
for index, item in enumerate(open_orders, 1):
    print(f"{index}) {item}")
    
choice_open_order=input("Enter the order ID to remove from stock:  ")
print("Order ID number is  " + str(choice_open_order))

found = None
for item in open_orders:
    if item.lower().replace("_", " ") == choice_open_order.lower().replace("_", " "):
       found=item
       break
     
if found:
    print(f"Processing {found}")
    open_orders.remove(found)
    print(f"Order ID {found} has been removed") 

else:
    print("Order not found")

 