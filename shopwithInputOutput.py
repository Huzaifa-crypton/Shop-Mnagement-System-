print("***********************************")
print("        SHOP MANAGEMENT SYSTEM     ")
print("***********************************")

item_name=""
item_price=0
item_saleprice=0
item_quantity=0


item_name=input("Enter name of item:")
item_price=float(input("Enter original price of item:"))
item_saleprice = float(input("Enter sale price of item:"))
item_quantity=float(input("Enter Qantity of item:"))

print("Sale Item")
item=input("enter name of item:")
quantity=int(input("enter quantity: "))
price = quantity * item_saleprice
print("Pay ",price)