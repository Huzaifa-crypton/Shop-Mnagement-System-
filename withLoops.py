import os
salesperson_name=""
salesperson_password=""
item_name=""
item_price=0
item_saleprice=0
item_quantity=0
total_sales=0
profit = 0
day1 = 0
day2 = 0
day = 0
while(True):
    os.system("cls")
    print("************************************************")
    print("            SHOP MANAGEMENT SYSTEM              ")
    print("************************************************")
    print("*****Hi there, welcome to the clothing shop*****")
    option1 = 0
    option2 = 0
    print("Please enter Username and Password")
    username=input("Enter Username: ")
    password=input("Enter Password: ")

    
    if username=="Admin" and password == "1234" :
        while(option1!=10):
            os.system("CLS")
            print("************************************************")
            print("            SHOP MANAGEMENT SYSTEM              ")
            print("************************************************")
            print(""" 
1. Add SalesPerson
2. View all salesperson
3. Replace Salesperson
4. Add items to stock
5. View added items
6. REPLACE ITEM
7. TOTAL SALE OF THE DAY
8. PROFIT FOR THE DAY
9. 10% DISCOUNT DAYS
10. EXIT
        """)
            option1 = int (input("Enter option number-->"))
            if option1 == 1 :
                os.system("CLS")
                print("************************************************")
                print("            SHOP MANAGEMENT SYSTEM              ")
                print("************************************************")
                salesperson_name=input("Enter name of salesperson:")
                salesperson_password=input("Enter password:")
                input("Press any key to continue")
            elif option1 == 2 :
                os.system("CLS")
                print("************************************************")
                print("            SHOP MANAGEMENT SYSTEM              ")
                print("************************************************")
                print("Details of salesperson:")
                print("Name              Password")
                print(salesperson_name,"              ",salesperson_password)
                input("Press any key to continue")
            elif option1 == 3 :
                os.system("CLS")
                print("************************************************")
                print("            SHOP MANAGEMENT SYSTEM              ")
                print("************************************************")
                print("Replace salesperson")
                salesperson_name=input("Enter name of salesperson:")
                salesperson_password=input("Enter password:")
                input("Press any key to continue")
            elif option1 == 4 :
                os.system("CLS")
                print("************************************************")
                print("            SHOP MANAGEMENT SYSTEM              ")
                print("************************************************")
                item_name=input("Enter name of item:")
                item_price=float(input("Enter original price of item:"))
                item_saleprice = float(input("Enter sale price of item:"))
                item_quantity=float(input("Enter Qantity of item:"))
                input("Press any key to continue")
            elif option1 == 5 :
                os.system("CLS")
                print("************************************************")
                print("            SHOP MANAGEMENT SYSTEM              ")
                print("************************************************")
                print("Details of items:")
                print("Name           OiginalPrice              SalePrice                       Quantity")
                print(item_name,"              ",item_price,"              ",item_saleprice,"                   ",item_quantity)   
                input("Press any key to continue")
            elif option1 == 6 :
                os.system("CLS")
                print("************************************************")
                print("            SHOP MANAGEMENT SYSTEM              ")
                print("************************************************")
                print("Replace item")
                item_name=input("Enter name of item:")
                item_price=float(input("Enter price of item:"))
                item_quantity=float(input("Enter Qantity of item:"))    
                input("Press any key to continue")
            elif option1 == 7 :
                print("Total sales of the day are -->",total_sales)
                input("Press any key to continue")
            elif option1 == 8 :
                print("Total profit for hte day is-->",profit)
                input("Press any key to continue")
            elif option1 == 9 :
                print ("Enter days for discount:")
                day1 = int (input( "Day 1: "))
                day2 = int (input( "Day 2: "))
                input("Press any key to continue")    
    elif password == salesperson_password and username == salesperson_name :
        while option2 !=6 :
            os.system("CLS")
            print("************************************************")
            print("            SHOP MANAGEMENT SYSTEM              ")
            print("************************************************")
            print("""
        ****Hi , hope your day is going well****
        Enter the option that you want to operate:

    1.	ENTER TODAY’S DAY
    2.	ENTER ITEM TO BE SOLD
    3.	CASH RECEIVED
    4.	BALANCE
    5.	VIEW ITEMS
    6.	EXIT


        """)
            option2=int(input("YOUR OPTION "))
            if option2 == 1 :
                day = int (input("enter todays day-->"))
            if (option2==2):
                os.system("CLS")
                item=input("enter name of item:")
                quantity=int(input("enter quantity: "))
                if(item == item_name and quantity <=item_quantity) :
                    if (day == day1 or day == day2) :
                        price = item_saleprice*quantity*.9
                        total_sales = total_sales +price
                        print("Pay ",price)
                    else :
                        price = item_saleprice*quantity
                        print("Pay ",price)
                else :
                    print("No item found")
                input("Press any key to continue")        
            elif option2 == 5 : 
                os.system("CLS")
                print("Details of salesperson:")
                print("Name           OrginalPrice              SalePrice                       Quantity")
                print(item_name,"              ",item_price,"              ",item_saleprice,"                   ",item_quantity)   
                input("Press any key to continue")
            elif option2 == 3 :
                os.system("CLS")
                cash = int (input("Enter cash received-->"))
            elif option2 == 4 :
                os.system("CLS")
                balace = cash - price
                if balance>=0 :
                    print("Pay back " , balance)
                else :
                    print("Customer  has to pay -->",balance*(-1))        
