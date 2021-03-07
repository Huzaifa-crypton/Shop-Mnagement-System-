salesperson_name=""
salesperson_password=""
item_name=""
item_price=0
item_saleprice=0
item_quantity=0

print("************************************************")
print("            SHOP MANAGEMENT SYSTEM              ")
print("************************************************")
print("*****Hi there, welcome to the clothing shop*****")
option = 0
print("Please enter Username and Password")
username=input("Enter Username: ")
password=input("Enter Password: ")

if username=="Admin" and password == "1234" :
    print("************************************************")
    print("            SHOP MANAGEMENT SYSTEM              ")
    print("************************************************")
    print("1. Add Items to Stock")
option = int (input("Enter option number-->"))
    if option == 1 :
        item_name=input("Enter name of item:")
        item_price=float(input("Enter original price of item:"))
        item_saleprice = float(input("Enter sale price of item:"))
        item_quantity=float(input("Enter Quantity of item:"))    
print("************************************************")
print("            SHOP MANAGEMENT SYSTEM              ")
print("************************************************")
print("*****Hi there, welcome to the clothing shop*****")
option = 0
print("Please enter Username and Password")
username=input("Enter Username: ")
password=input("Enter Password: ")

elif password == salesperson_password and username == salesperson_name :
    print("************************************************")
    print("            SHOP MANAGEMENT SYSTEM              ")
    print("************************************************")
    print("""

****Hi (SALESPERSON USERNAME), hope your day is going well****
Enter the option that you want to operate:

1.	ADD ITEM TO BE SOLD
""")
    option=int(input("YOUR OPTION "))
    if (option==1):
        item=input("enter name of item:")
        quantity=int(input("enter quantity: "))
        if(item == item_name and quantity <=item_quantity) :
            price = item_saleprice*quantity
            print("Pay ",price)
        else :
            print("No item found")   
        input("Press any key to continue")     