import os
size = 5                               #fixed size for 5 salesperson and 5 items
username_salesperson = []
items=[]
password_salesperson=[]
rem_quantity=[]                     #total remaining quantity of each item
sold_quantity=[0,0,0,0,0]        #sum of number of items sold by each salesperson
sold_quantity1=[0,0,0,0,0]    
sold_quantity2=[0,0,0,0,0]
sold_quantity3=[0,0,0,0,0]
sold_quantity4=[0,0,0,0,0]
sold_quantity5=[0,0,0,0,0]
discounted_price=[]                 #sum of discounted price of each salesperson
discounted_price1=[]
discounted_price2=[]
discounted_price3=[]
discounted_price4=[]
discounted_price5=[]
diff_price=[]                       #to calculate profit
total_amount=[]                     #sum of total amount of every salesperson(before discount)
total_amount1=[]
total_amount2=[]
total_amount3=[]
total_amount4=[]
total_amount5=[]
original_price=[]                   #original price of each item
sale_price=[]                       #selling price of each item
copy_sale_price=[]                  #sorting sale price array
sell_idx=0
cash=0
balance=0 
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
        while(option1!=11):
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
7. Sort Items (Price)
8. TOTAL SALE OF THE DAY
9. PROFIT FOR THE DAY
10. 10% DISCOUNT DAYS
11. EXIT
        """)
            option1 = int (input("Enter option number-->"))
            if option1 == 1 :
                os.system("CLS")
                print("************************************************")
                print("            SHOP MANAGEMENT SYSTEM              ")
                print("************************************************")
                salesperson_name=input("Enter name of salesperson:")
                salesperson_password=input("Enter password:")
                username_salesperson.append(salesperson_name)
                password_salesperson.append(salesperson_password)    
                input("Press any key to continue")
            elif option1 == 2 :
                os.system("CLS")
                print("************************************************")
                print("            SHOP MANAGEMENT SYSTEM              ")
                print("************************************************")
                print("Details of salesperson:")
                print("Sr.               Name              Password")
                for i in range (len(username_salesperson)) :
                    print(i+1,"              ",username_salesperson[i] ,"              ",password_salesperson[i])
                input("Press any key to continue")
            elif option1 == 3 :
                os.system("CLS")
                print("************************************************")
                print("            SHOP MANAGEMENT SYSTEM              ")
                print("************************************************")
                print("Details of salesperson:")
                print("Sr.               Name              Password")
                for i in range (0,len(username_salesperson)) :
                    print(i+1,"              ",username_salesperson[i] ,"              ",password_salesperson[i])
                opt=int (input("Enter Sr. number of salesperson you want to change: "))
                username_salesperson[opt-1]=input("Enter name of salesperson:")
                password_salesperson[opt-1]=input("Enter password:")
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
                items.append(item_name)
                sale_price.append(item_saleprice)
                copy_sale_price.append(item_saleprice)
                original_price.append(item_price)
                rem_quantity.append(item_quantity)
                input("Press any key to continue")
            elif option1 == 5 :
                os.system("CLS")
                print("************************************************")
                print("            SHOP MANAGEMENT SYSTEM              ")
                print("************************************************")
                print("Details of items:")
                print("Sr.           Name           OiginalPrice              SalePrice                       Quantity")
                for i in range(0 , len(items)):
                    print(i+1,"              ",items[i],"              ",original_price[i],"              ",sale_price[i],"                   ",rem_quantity[i])    
                input("Press any key to continue")
            elif option1 == 6 :
                os.system("CLS")
                print("************************************************")
                print("            SHOP MANAGEMENT SYSTEM              ")
                print("************************************************")
                print("Details of items:")
                print("Sr.           Name           OiginalPrice              SalePrice                       Quantity")
                for i in range(0 , len(items)):
                    print(i+1,"              ",items[i],"              ",original_price[i],"              ",sale_price[i],"                   ",rem_quantity[i])    
                opt=int (input("Enter Sr. number of salesperson you want to change: "))
                items[opt-1]=input("Enter name of item:")
                original_price[opt-1]=float(input("Enter original price of item:"))
                sale_price[opt-1] = float(input("Enter sale price of item:"))
                rem_quantity[opt-1]=float(input("Enter Qantity of item:"))
                input("Press any key to continue")
            elif option1 == 7 :
                os.system("cls")
                print("************************************************")
                print("            SHOP MANAGEMENT SYSTEM              ")
                print("************************************************")
                for i in range(0 , len(copy_sale_price)) :
                    for a in range(0 , len(copy_sale_price)):
                        if (copy_sale_price[i] < copy_sale_price[a]) :
                            p = copy_sale_price[a]
                            copy_sale_price[a] = copy_sale_price [n]
                            copy_sale_price[n] = p
                print("Details of the items from high to low price are:")
                print("Sr.           Name           OiginalPrice              SalePrice                       Quantity") 
                for i in range (0 , len(copy_sale_price)) :
                    for a in range (0 , len(copy_sale_price)) :
                        if (copy_sale_price[i] == sale_price[a]) :
                            print(i+1,"              ",items[a],"              ",original_price[a],"              ",sale_price[a],"                   ",rem_quantity[a])
                input ("Press any key to continue")
            elif option1 == 10 :
                print("Enter days on which 10 percent  discount is to be given:")
                day1 = int (input("Enter day 1 :"))
                day2 = int (input("Enter day 2 :"))
                input ("Press any key to continue")            
    for i in range (0 , len(username_salesperson)) :
        if (username == username_salesperson[i] and password == password_salesperson[i]) :
            while option2 != 11 :
                os.system("CLS")
                print("************************************************")
                print("            SHOP MANAGEMENT SYSTEM              ")
                print("************************************************")
                print("""
        ****Hi , hope your day is going well****
        Enter the option that you want to operate:

    1.	ENTER TODAY’S DAY
    2.	ADD ITEM TO BE SOLD
    3.	Add QUANTITY OF ITEM
    4.	TOTAL AMOUNT
    5.	DISCOUNTED AMOUNT
    6.	PAYABLE AMOUNT
    7.  CASH RECEIVED
    8.  BALANCE
    9.  DAILY SALE REPORT
    10. VIEW ITEMS
    11. EXIT 


        """)
                option2=int(input("YOUR OPTION "))
                if option2 == 1 :
                    day = int (input("enter todays day-->"))
                elif option2 == 2 :
                    flag =0
                    item = input("Enter name of item to be sold: ")
                    for a in range (0 , len(item_name)) :
                        if (item == item_name[a]) :
                            flag = 1                        
                            sell_idx = a
                    if flag == 1 :
                        print("Item is available")
                    elif flag == 0 :
                        print("Item is not available in stock")
                elif option2 == 3 :
                    qnt = int ("Enter quantity of item to be sold: ")
                    if (qnt <= rem_quantity[sell_idx]) :
                        rem_quantity[sell_idx] = rem_quantity[sell_idx] - qnt
                        if i == 0 :
                            sold_quantity1[sell_idx] = sold_quantity1[sell_idx] + qnt 
                        if i == 1 :
                            sold_quantity2[sell_idx] = sold_quantity2[sell_idx] + qnt
                        if i == 2 :
                            sold_quantity3[sell_idx] = sold_quantity3[sell_idx] + qnt
                        if i == 3 :
                            sold_quantity4[sell_idx] = sold_quantity4[sell_idx] + qnt
                        if i == 4 :                                                 
                            sold_quantity5[sell_idx] = sold_quantity5[sell_idx] + qnt                 
                    elif qnt > rem_quantity[sell_idx] :
                        print(rem_quantity[sell_idx]," items are left.")
                elif option2 == 4 :
                    if i == 0 :
                        total_amount1[sell_idx]=total_amount1[sell_idx] + sold_quantity1[sell_idx]
                        print("Total Amount--> ",total_amount1[sell_idx])
                    if i == 1 :
                        total_amount2[sell_idx]=total_amount2[sell_idx] + sold_quantity2[sell_idx]
                        print("Total Amount--> ",total_amount2[sell_idx])
                    if i == 2 :
                        total_amount3[sell_idx]=total_amount3[sell_idx] + sold_quantity3[sell_idx]
                        print("Total Amount--> ",total_amount3[sell_idx])
                    if i == 3 :
                        total_amount4[sell_idx]=total_amount4[sell_idx] + sold_quantity4[sell_idx]
                        print("Total Amount--> ",total_amount4[sell_idx])
                    if i == 4 :                                          
                        total_amount5[sell_idx]=total_amount5[sell_idx] + sold_quantity5[sell_idx]
                        print("Total Amount--> ",total_amount5[sell_idx])
                elif option2 == 5 :
                    if ((day==day1) or (day==day2)) :
                        print("YOU HAVE GOT 10% DISCOUNT ON TOTAL AMOUNT")
                        if i==0 :
                            discounted_price1[sell_idx]=total_amount1[sell_idx]*0.9
                            print("Discounted amount= ",discounted_price1[sell_idx])          
                        elif i==1 :
                            discounted_price2[sell_idx]=total_amount2[sell_idx]*0.9
                            print("Discounted amount= ",discounted_price2[sell_idx])
                        elif i==2 :
                            discounted_price3[sell_idx]=total_amount3[sell_idx]*0.9
                            print("Discounted amount= ",discounted_price3[sell_idx])
                        elif i==3 :
                            discounted_price4[sell_idx]=total_amount4[sell_idx]*0.9
                            print("Discounted amount= ",discounted_price4[sell_idx])
                        elif i==4 :
                            discounted_price5[sell_idx]=total_amount5[sell_idx]*0.9
                            print("Discounted amount= ",discounted_price5[sell_idx])
                    else :
                        if i==0 :
                            print("No discount today")
                            discounted_price1[sell_idx]=total_amount1[sell_idx];
                            print("Discounted amount= ",discounted_price1[sell_idx])       
                        if i==1 :
                            print("No discount today")
                            discounted_price2[sell_idx]=total_amount2[sell_idx];
                            print("Discounted amount= ",discounted_price2[sell_idx])
                        if i==2 :
                            print("No discount today")
                            discounted_price3[sell_idx]=total_amount3[sell_idx];
                            print("Discounted amount= ",discounted_price3[sell_idx])
                        if i==3 :
                            print("No discount today")
                            discounted_price4[sell_idx]=total_amount4[sell_idx];
                            print("Discounted amount= ",discounted_price4[sell_idx])
                        if i==4 :
                            print("No discount today")
                            discounted_price5[sell_idx]=total_amount5[sell_idx];
                            print("Discounted amount= ",discounted_price5[sell_idx])
                    input("press any key to continue")           
                elif option2 == 6 :
                    if i==0 :     
                        print("Payable amount= ",discounted_price1[sell_idx])       
                    elif i==1 :     
                        print("Payable amount= ",discounted_price2[sell_idx]) 
                    elif i==2 :     
                        print("Payable amount= ",discounted_price3[sell_idx]) 
                    elif i==3 :     
                        print("Payable amount= ",discounted_price4[sell_idx]) 
                    elif i==4 :     
                        print("Payable amount= ",discounted_price5[sell_idx])
                elif option2 == 7 :
                    cash=int(input("Cash received-->"))
                    input("press any key to continue")
                elif option2 == 8 :
                    if i == 0 :
                        balance = cash - discounted_price1[sell_idx]
                    elif i == 1 :
                        balance = cash - discounted_price2[sell_idx]
                    elif i == 2 :
                        balance = cash - discounted_price3[sell_idx]
                    elif i == 3 :
                        balance = cash - discounted_price4[sell_idx]
                    elif i == 4 :
                        balance = cash - discounted_price5[sell_idx]                
                    if balance > 0 :
                        print("PAY BACK ",balance," Rupees to customer.")
                    elif balance < 0 :
                        print("Customer has to pay ",(-1)*balance," Rupees more.")     
                
                elif option2 == 10 :
                    os.system("CLS")
                    print("************************************************")
                    print("            SHOP MANAGEMENT SYSTEM              ")
                    print("************************************************")
                    print("Details of items:")
                    print("Sr.           Name           OiginalPrice              SalePrice                       Quantity")
                    for a in range(0 , len(items)):
                        print(a+1,"              ",items[a],"              ",original_price[a],"              ",sale_price[a],"              ",rem_quantity[a])

                elif option2 == 9 :
                    print("SR.NO","         ","ITEM_NAME","         ","QUANTITY_SOLD","         ","ACTUAL_AMOUNT","         ","SOLD_AMOUNT","         ")
                    if i==0 :
                        for a in range(0 , len(item)) :
                            print(a+1,"                ",items[a],"                 ",sold_quantity1[a],"              ",total_amount1[a],"              ",discounted_price1[a],"         ")
                    elif i==1 :
                        for a in range(0 , len(item)) :
                            print(a+1,"                ",items[a],"                 ",sold_quantity2[a],"              ",total_amount2[a],"              ",discounted_price2[a],"         ")
                    if i==2 :
                        for a in range(0 , len(item)) :
                            print(a+1,"                ",items[a],"                 ",sold_quantity3[a],"              ",total_amount3[a],"              ",discounted_price3[a],"         ")
                    if i==3 :
                        for a in range(0 , len(item)) :
                            print(a+1,"                ",items[a],"                 ",sold_quantity4[a],"              ",total_amount4[a],"              ",discounted_price4[a],"         ")
                    if i==4 :
                        for a in range(0 , len(item)) :
                            print(a+1,"                ",items[a],"                 ",sold_quantity5[a],"              ",total_amount5[a],"              ",discounted_price5[a],"         ")                            
            