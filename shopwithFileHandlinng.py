import os
size = 5                               #fixed size for 5 salesperson and 5 items
username_salesperson = [" " , " "  , " " , " " , " "]
items=[" " , " "  , " " , " " , " "]
password_salesperson=[0,0,0,0,0]
rem_quantity=[0,0,0,0,0]                     #total remaining quantity of each item
sold_quantity=[0,0,0,0,0]        #sum of number of items sold by each salesperson
sold_quantity1=[0,0,0,0,0]    
sold_quantity2=[0,0,0,0,0]
sold_quantity3=[0,0,0,0,0]
sold_quantity4=[0,0,0,0,0]
sold_quantity5=[0,0,0,0,0]
discounted_price=[0,0,0,0,0]                 #sum of discounted price of each salesperson
discounted_price1=[0,0,0,0,0]
discounted_price2=[0,0,0,0,0]
discounted_price3=[0,0,0,0,0]
discounted_price4=[0,0,0,0,0]
discounted_price5=[0,0,0,0,0]
diff_price=[0,0,0,0,0]                       #to calculate profit
total_amount=[0,0,0,0,0]                     #sum of total amount of every salesperson(before discount)
total_amount1=[0,0,0,0,0]
total_amount2=[0,0,0,0,0]
total_amount3=[0,0,0,0,0]
total_amount4=[0,0,0,0,0]
total_amount5=[0,0,0,0,0]
original_price=[0,0,0,0,0]                   #original price of each item
sale_price=[0,0,0,0,0]                       #selling price of each item
copy_sale_price=[0,0,0,0,0]                  #sorting sale price array
balance=0


#GLOBAL Variables
total_sale=0                              #total sales of the day
total_profit_today = 0                  
flag1 = 0                                 #flag for salesperson
opt = 0
opt1 = 0
flag = 0                                  #flag for added items
option = 0                                #menu OPTION
option1 = 0                               #replace salesperson,items
idx = -1                                 #salesperson index
idx1 = -1                                  #added items index
sell_idx = -1                             #index of item being sold    
day=0
day1=0
day2=0                                    #day=day today  ,  day1=discount day1 , day2=discount day2
quantity=0     
cash=0
current_salesperson=-1                    #indexx of salesperson loggedin


def get_title() :
    print("===============================================")
    print("             SHOP MANAGEMENT SYSTEM            ")
    print("===============================================")
    print("\n")

def press_key() :
    input("Press any key to continue")
    print("\n")


def get_field(record , place) :
    comma=0
    value=""
    i=0
    for r in range(0 , len(record)) :
        c=record[r]
        if c==',' :
            comma=comma+1
        elif comma==place :
            value=value+c
    return value

def admin_menu() :
    os.system("cls")
    get_title()
    print("*****Hi ADMIN,hope your day is going well******")
    print("\n")
    print("Enter the option you want to operate:")
    print("\n")
    print(" 1.  ADD SALESPERSON")
    print(" 2.  VIEW ADDED SALESPERSON")
    print(" 3.  REPLACE SALESPERSON")
    print(" 4.  ADD ITEMS TO STOCK")
    print(" 5.  VIEW ADDED ITEMS")
    print(" 6.  REPLACE ITEMS")
    print(" 7.  SORT ITEMS(PRICE)")
    print(" 8.  TOTAL SALES OF THE DAY")
    print(" 9.  PROFIT FOR THE DAY")
    print(" 10. 10% DISCOUNT DAYS")
    print(" 11. EXIT")
    print("\n")
    option = int (input("Your option--> "))

    return option

def limit_salesperson() :
        global flag1
        global idx
        idx=4
        print("NO MORE SALESPERSON CAN BE ADDED, LIMIT OF 5 HAS REACHED.")
        print("TO ADD NEW SALESPERSON YOU HAVE TO REPLACE HIM WITH THE  ")
        print("             PREVIOUSLY ADDED SALESPERSON                ")
        flag1=1
        press_key()    

def save_salesperson() :
    global idx
    global username_salesperson
    global password_salesperson
    file1 = open("salesperson.txt" , "w")
    for s in range(0 ,idx+1) :
        record = username_salesperson[s]
        record = record + "," +str(password_salesperson[s])
        print(record , file=file1 , sep="\n")
    file1.close()

def add_salesperson_load(uname , password , index) :
    global username_salesperson
    global password_salesperson
    username_salesperson[index]=uname 
    password_salesperson[index]=password

def add_items_load(item ,  quantity , org_price , s_price , q1, q2, q3, q4, q5 ):
    global idx1
    global items
    global original_price
    global sale_price
    global rem_quantity
    global diff_price
    global sold_quantity
    global sold_quantity1
    global sold_quantity2
    global sold_quantity3
    global sold_quantity4
    global sold_quantity5
    items[idx1]=item
    rem_quantity[idx1]=quantity
    copy_sale_price[idx1]=s_price
    sale_price[idx1]=s_price
    original_price[idx1]=org_price
    diff_price[idx1]=sale_price[idx1]-original_price[idx1]
    sold_quantity1[idx1]=q1
    sold_quantity2[idx1]=q2
    sold_quantity3[idx1]=q3
    sold_quantity4[idx1]=q4
    sold_quantity5[idx1]=q5

def load_items() :
    global idx1
    file2 = open("items.txt" , "r")
    idx1=-1
    records = file2.read().splitlines()
    for record in records :
        idx1 = idx1 +1
        i=get_field(record,0)
        o_price=float(get_field(record,1))
        s_price=float(get_field(record,2))
        q=int(get_field(record,3))
        q1=int(get_field(record,4))
        q2=int(get_field(record,5))
        q3=int(get_field(record,6))
        q4=int(get_field(record,7))
        q5=int(get_field(record,8))
        add_items_load(i , q , o_price , s_price , q1, q2, q3, q4, q5)
    file2.close()

def add_salesperson(uname , password , index) :
    global username_salesperson
    global password_salesperson
    username_salesperson[index]=uname 
    password_salesperson[index]=password
    save_salesperson()


def load_salesperson() :
    global idx
    global current_salesperson
    file1 = open("salesperson.txt" , "r")
    idx=-1
    records = file1.read().splitlines() 
    for record in records:
        idx = idx +1
        u_salesperson=get_field(record,0)
        p_salesperson=int(get_field(record,1))
        add_salesperson_load(u_salesperson , p_salesperson ,idx)
    file1.close()
def add_salespersonUI() :
    #MAXIMUM 5 SALESPERSONS CAN BE ADDED....AFTER 5,REWRITING STARTS
    global idx
    global flag1
    os.system("CLS")
    get_title() 
    idx = idx + 1
    if idx>=5 and flag1==0 :
        limit_salesperson()
    if flag1==0 :
        print("Enter USERNAME and PASSWORD for the new salesperson:")
        uname_salesperson= input("USERNAME: ")
        pass_salesperson = int (input("PASSWORD: "))
        add_salesperson(uname_salesperson , pass_salesperson , idx)


def view_salesperson() :
    os.system("CLS")
    global username_salesperson
    global password_salesperson
    global idx
    serial=0
    print("Details of the added salesperson are:")
    print("\n")
    print("SR.NO","       ","USERNAMES","        ","PASSWORDS","         ")
    for a in range (0 , idx+1) :
        serial = serial + 1
        if serial == 6 :
            serial = 0 
        print(serial,"           ",username_salesperson[a],"          ",password_salesperson[a],"        ")
    press_key()

def replace_salesperson() :
    os.system("cls") 
    serial=0
    global idx
    global username_salesperson
    global password_salesperson
    print("Details of the added salesperson are:")
    print("\n")
    print("SR.NO","       ","USERNAMES","        ","PASSWORDS","         ")
    for a in range(0 , idx +1) :
        serial = serial +1
        if serial==6 :
            serial=0
        print(serial , "               " , username_salesperson[a] , "             " , password_salesperson[a] , "        ")
    
    print("\n")
    print("Enter the SR.NO of the salesperson which is to be replaced by a new one: ")
    print("\n")
    option1 = int (input("YOUR OPTION--> "))
    uname_salesperson = input("Enter new USERNAME: ")
    pass_salesperson = int (input("Enter new PASSWORD: "))
    username_salesperson[(option1-1)]=uname_salesperson
    password_salesperson[(option1-1)]=pass_salesperson
    save_salesperson()
    print("<<<<<<<<<Salesperson has been updated>>>>>>>>>>")
    press_key()

def limit_items() :
    print("Sorry, our shop is not having more space to add new items")
    print("To add new items, replace it with the items present previously")
    global idx1
    global flag
    idx1=4
    flag=1
    press_key()
def save_items() :
    global idx1
    global items
    global original_price
    global sale_price
    global rem_quantity
    global sold_quantity
    global sold_quantity1
    global sold_quantity2
    global sold_quantity3
    global sold_quantity4
    global sold_quantity5
    file2=open("items.txt" , "w")
    for s in range (0 , idx1 + 1) :
        record=items[s]
        record=record + "," + str(original_price[s])
        record=record + "," + str(sale_price[s])
        record=record + "," + str(rem_quantity[s])
        record=record + "," + str(sold_quantity1[s])
        record=record + "," + str(sold_quantity2[s])
        record=record + "," + str(sold_quantity3[s])
        record=record + "," + str(sold_quantity4[s])
        record=record + "," + str(sold_quantity5[s])
        print(record , file=file2 , sep="\n")
    file2.close()

def add_items( item ,  quantity ,  org_price ,  s_price , index) :
    global items
    global rem_quantity
    global copy_sale_price
    global sale_price
    global original_price
    global diff_price
    items[index]=item
    rem_quantity[index]=quantity
    copy_sale_price[index]=s_price
    sale_price[index]=s_price
    original_price[index]=org_price
    diff_price[index]=sale_price[index]-original_price[index]
    save_items()


def add_itemsUI() :
    os.system("CLS")
    get_title()
    global flag
    global idx1
    global quantity
    flag=0
    if idx1>=5 and flag==0 :
        limit_items()    
    if flag==0 :
        print("Add details of the new item:")
        item_name = input("Item Name     :")  
        org_price = float(input("Original Price    :"))
        s_price = float(input("Sale Price    :"))
        quantity = int(input("Quantity    :"))
        
        if (s_price and quantity and org_price) > 0 :
            idx1 = idx1 +1
            add_items(item_name , quantity , org_price , s_price , idx1 )
            print("Item added successfully")
            press_key()
        elif (s_price and quantity and org_price) < 0 :
            print("Invalid item information added")
            press_key()


def view_items() :
    os.system("cls")
    get_title()
    global idx1
    global items
    global rem_quantity
    global copy_sale_price
    global sale_price
    global original_price
    global diff_price
    print("Details of the added items are: ")
    print("SR.NO","       ","ITEMS","        ","REM_QUANTITY","         ","ORIGINAL_PRICE","         ","SALE_PRICE","         ")
    serial=0
    for a in range(0 ,idx1+1) :
        serial=serial+1
        if serial==6 :
            serial=0
        print(serial,"           ",items[a],"            ",rem_quantity[a],"                       ",original_price[a],"                 ",sale_price[a],"        ")
    press_key()


def replace_items() :
    os.system("cls")
    get_title()
    print("Details of the added items are: ")
    print("SR.NO","       ","ITEMS","        ","REM_QUANTITY","         ","ORIGINAL_PRICE","         ","SALE_PRICE","         ")
    serial=0
    for a in range(0 ,idx1+1) :
        serial=serial+1
        if serial==6 :
            serial=0
        print(serial,"           ",items[a],"            ",rem_quantity[a],"                       ",original_price[a],"                 ",sale_price[a],"        ")
    print("\n")
    print("Enter the SR.NO of the item that is to be replaced: ")
    option1 = int(input("YOUR OPTION--> "))
    print("\n")
    print("Add details of the new item:")
    item_name = input("Item Name     :")  
    org_price = float(input("Original Price    :"))
    s_price = float(input("Sale Price    :"))
    quantity = int(input("Quantity    :"))
        
    items[(option1-1)]=item_name
    rem_quantity[(option1-1)]=quantity
    copy_sale_price[(option1-1)]=s_price
    sale_price[(option1-1)]=s_price
    original_price[(option1-1)]=org_price
    diff_price[(option1-1)]=sale_price[(option1-1)]-original_price[(option1-1)]
    save_items()
    print("<<<<<<<<<ITEM UPDATED SUCCESSFULLY>>>>>>>>>>>")
    press_key()

def print_sort_items() :
    os.system("cls")
    get_title()
    global idx1
    global items
    global rem_quantity
    global copy_sale_price
    global sale_price
    global original_price
    global diff_price
    print("Details of the items from high to low price are: ")
    print("\n")
    print("SR.NO","       ","ITEMS","        ","REM_QUANTITY","         ","ORIGINAL_PRICE","         ","SALE_PRICE","         ")
    serial=0
    for a in range (0 , idx1 +1) :
        for n in range (0 , idx1 +1) :
            if copy_sale_price[a]==sale_price[n] :
                serial =serial +1
                print(serial ,"           ",items[n],"           ",rem_quantity[n],"                 ",original_price[n],"                 ",sale_price[n]<<"        ")

def sort_items() :
    global idx1
    global copy_sale_price
    for a in range (0 , idx1 +1) :
        for n in range (0 , idx1+1) :
            if copy_sale_price[n] < copy_sale_price[a] :
                current_value=copy_sale_price[a]
                copy_sale_price[a]=copy_sale_price[n]
                copy_sale_price[n]=current_value
    print_sort_items()
    press_key()

def discount_days() :
    os.system("cls")
    get_title()  
    global day1
    global day2
    day1 = int (input("Enter the 1st day on which 10% discount is to be given on the total payable amount: "))
    day2 = int (input("Enter the 2nd day on which 10% discount is to be given on the total payable amount: "))  
    press_key()  


def salesperson_menu() :
    os.system("cls")
    get_title()
    global username_salesperson
    global current_salesperson
    print("*****Hi ",username_salesperson[current_salesperson]," ,hope your day is going well******")
    print("Enter the option you want to operate:")
    print("\n")
    print(" 1.  ENTER TODAY'S DAY")
    print(" 2.  ADD ITEM TO BE SOLD")
    print(" 3.  ADD QUANTITY OF THE ITEM")
    print(" 4.  TOTAL AMOUNT")
    print(" 5.  DISCOUNTED AMOUNT")
    print(" 6.  PAYABLE AMOUNT")
    print(" 7.  CASH RECEIVED")
    print(" 8.  BALANCE")
    print(" 9.  DAILY SALE REPORT")
    print(" 10. VIEW ITEMS")
    print(" 11. EXIT")
    print("\n")
    option = int (input("Your option-->"))
    return option


def day_today() :
    os.system("cls")
    get_title()
    global day
    global day1
    global day2
    day = int (input(" Enter the day today-->"))
    print("\n")
    print("Discount day= ",day1) 
    print("Discount day= ",day2)
    press_key()


def print_total_sale() :
    serial=0
    global idx1
    global sold_quantity
    global sold_quantity1
    global sold_quantity2
    global sold_quantity3
    global sold_quantity4
    global sold_quantity5
    global total_amount
    global total_amount1
    global total_amount2
    global total_amount3
    global total_amount4
    global total_amount5
    global discounted_price
    global discounted_price1
    global discounted_price2
    global discounted_price3
    global discounted_price4
    global discounted_price5
    global items
    global rem_quantity
    global copy_sale_price
    global sale_price
    global original_price
    global diff_price

    for  a in range (0 , idx1+1) :
        sold_quantity[a]=sold_quantity1[a]+sold_quantity2[a]+sold_quantity3[a]+sold_quantity4[a]+sold_quantity5[a]
        total_amount[a]=total_amount1[a]+total_amount2[a]+total_amount3[a]+total_amount4[a]+total_amount5[a]
        discounted_price[a]=discounted_price1[a]+discounted_price2[a]+discounted_price3[a]+discounted_price4[a]+discounted_price5[a]
        serial = serial +1
        if serial==6 :
            serial=0
        print(serial,"           ",items[a],"          ",sold_quantity[a],"          ",total_amount[a],"        ",discounted_price[a],"         ")
    


def total_sale_today() :
    os.system("cls")
    get_title()
    global total_sale
    global idx1
    global discounted_price
    total_sale=0
    print("Details of sold items are: ")
    print("SR.NO","       ","ITEMS","        ","QUANTITY","         ","ACTUAL TOTAL PRICE","         ","SOLD PRICE","         ")
    
    print_total_sale()   
    for a in range (0 , idx1 +1) :
        total_sale=total_sale+discounted_price[a]
    print("\n")
    print("TOTAL SALE OF THE DAY= ",total_sale)
    press_key()


def item_present(item , index):
    global items
    global rem_quantity
    if item==items[index] and rem_quantity[index]>0 :
        return True
    else :
        return False

def item_name() :
    os.system("cls")
    get_title()
    global flag  
    global idx1
    global sell_idx
    flag=0
    item = input("Enter name of item: ")

    for a in range (0 ,  idx1+1) :
        if item_present(item , a) :
            flag=1
            sell_idx=a
    if flag==0 :
        print("Item is not available")
    elif flag==1 :
        print("Item is available")
    press_key()

def remaining_quantity(quantity ,  index) :
    global rem_quantity
    if quantity>rem_quantity[index] :
        return True
    else :
        return False

def sold_quantity_salesperson() :
    global sell_idx
    global current_salesperson
    q=sell_idx
    if current_salesperson==0  :
        sold_quantity1[q]=sold_quantity1[q]+quantity
    elif current_salesperson==1  :
        sold_quantity2[q]=sold_quantity2[q]+quantity
    elif current_salesperson==2  :
        sold_quantity3[q]=sold_quantity3[q]+quantity
    elif current_salesperson==3  :
        sold_quantity4[q]=sold_quantity4[q]+quantity
    elif current_salesperson==4  :
        sold_quantity5[q]=sold_quantity5[q]+quantity               
    save_items()
    

def quantity_of_items() :
    os.system("cls")
    get_title()
    global quantity
    global sell_idx
    global rem_quantity
    global items
    quantity = int (input("Enter  number of items being sold: "))
    q=sell_idx
    if quantity<1 :
        print("Enter correct number of items  ")
    elif remaining_quantity(quantity , q) :
        print("Sorry, only ",rem_quantity[q]," ",items[q],"  are present.")
    elif (remaining_quantity(quantity , q)==False) :
        rem_quantity[q]=rem_quantity[q]-quantity
        save_items()
        sold_quantity_salesperson()
    press_key()
    return quantity    


def actual_amount() :
    os.system("cls")
    get_title()
    global sell_idx
    global current_salesperson
    global total_amount1
    global total_amount2
    global total_amount3
    global total_amount4
    global total_amount5
    global sold_quantity1
    global sold_quantity2
    global sold_quantity3
    global sold_quantity4
    global sold_quantity5

    q=sell_idx
    if current_salesperson==0 :
        total_amount1[q]=sale_price[q]*sold_quantity1[q]
        print("Total Amount= ",total_amount1[q])
    elif current_salesperson==1 :
        total_amount2[q]=sale_price[q]*sold_quantity2[q]
        print("Total Amount= ",total_amount2[q])
    elif current_salesperson==2 :
        total_amount3[q]=sale_price[q]*sold_quantity3[q]
        print("Total Amount= ",total_amount3[q])
    elif current_salesperson==3 :
        total_amount4[q]=sale_price[q]*sold_quantity4[q]
        print("Total Amount= ",total_amount4[q])
    elif current_salesperson==4 :
        total_amount5[q]=sale_price[q]*sold_quantity5[q]
        print("Total Amount= ",total_amount5[q])                    
    press_key()

def discounted_amount() :
    os.system("cls")
    get_title()
    global sell_idx
    q=sell_idx
    global current_salesperson
    global day1
    global day
    global day2
    global discounted_price1
    global discounted_price2
    global discounted_price3
    global discounted_price4
    global discounted_price5
    global total_amount1
    global total_amount2
    global total_amount3
    global total_amount4
    global total_amount5

    if day==day1 or day==day2 :
        print("YOU HAVE GOT 10% DISCOUNT ON TOTAL AMOUNT")
        if current_salesperson==0 :
            discounted_price1[q]=total_amount1[q]*0.9
            print("Discounted amount= ",discounted_price1[q])          
        elif current_salesperson==1 :
            discounted_price2[q]=total_amount2[q]*0.9
            print("Discounted amount= ",discounted_price2[q])          
        
        elif current_salesperson==2 :
            discounted_price3[q]=total_amount3[q]*0.9
            print("Discounted amount= ",discounted_price3[q])          
        
        elif current_salesperson==3 :
            discounted_price4[q]=total_amount4[q]*0.9
            print("Discounted amount= ",discounted_price4[q])          
        
        elif current_salesperson==4 :
            discounted_price5[q]=total_amount5[q]*0.9
            print("Discounted amount= ",discounted_price5[q])          
        
    else :
        if current_salesperson==0 :
            print("No discount today")
            discounted_price1[q]=total_amount1[q]
            print("Discounted amount= ",discounted_price1[q])
        elif current_salesperson==1 :
            print("No discount today")
            discounted_price2[q]=total_amount2[q]
            print("Discounted amount= ",discounted_price2[q])
        elif current_salesperson==2 :
            print("No discount today")
            discounted_price3[q]=total_amount3[q]
            print("Discounted amount= ",discounted_price3[q])
        elif current_salesperson==3 :
            print("No discount today")
            discounted_price4[q]=total_amount4[q]
            print("Discounted amount= ",discounted_price4[q])
        elif current_salesperson==4 :
            print("No discount today")
            discounted_price5[q]=total_amount5[q]
            print("Discounted amount= ",discounted_price5[q])                       
        
    press_key()

def total_payable_amount() :
    os.system("cls")
    get_title()
    global current_salesperson
    global sell_idx
    global discounted_price1
    global discounted_price2
    global discounted_price3
    global discounted_price4
    global discounted_price5
    if current_salesperson==0 : 
        print("Total payable amount= ",discounted_price1[sell_idx])
    elif current_salesperson==1: 
        print("Total payable amount= ",discounted_price2[sell_idx])
    elif current_salesperson==2 : 
        print("Total payable amount= ",discounted_price3[sell_idx])
    elif current_salesperson==3 : 
        print("Total payable amount= ",discounted_price4[sell_idx])
    elif current_salesperson==4 : 
        print("Total payable amount= ",discounted_price5[sell_idx])
        
    
    press_key()

def profit_today() :
    os.system("cls")
    get_title()
    total_profit_today=0
    global idx1
    global sold_quantity1
    global sold_quantity2
    global sold_quantity3
    global sold_quantity4
    global sold_quantity5
    global diff_price
    for a in range (0 , idx1+1) :
        total_profit_today = total_profit_today + (diff_price[a]*sold_quantity1[a]) + (diff_price[a]*sold_quantity2[a]) + (diff_price[a]*sold_quantity3[a]) + (diff_price[a]*sold_quantity4[a]) + (diff_price[a]*sold_quantity5[a])
    print("Profit today= ",total_profit_today)
    if total_profit_today<1000 :
         print("OHHH! NEVERMIND, it was a BAD SALES DAY.")
    else :
         print("SEEMS IT WAS A GOOD SALES DAY.")
    press_key()

def cash_received() :
    os.system("cls")
    get_title()
    global cash
    cash = int (input("CASH RECEIVED-->"))
    press_key()
    
def daily_salereport() :
    os.system("cls")
    get_title()
    global current_salesperson
    global idx1
    global sold_quantity1
    global sold_quantity2
    global sold_quantity3
    global sold_quantity4
    global sold_quantity5
    global total_amount1
    global total_amount2
    global total_amount3
    global total_amount4
    global total_amount5
    global discounted_price1
    global discounted_price2
    global discounted_price3
    global discounted_price4
    global discounted_price5
    print("SR.NO         ITEM_NAME         QUANTITY_SOLD         ACTUAL_AMOUNT         SOLD_AMOUNT         ")
    serial=0
    if current_salesperson==0 :
        for a in range (0 , idx1 +1) :
            serial=serial +1
            print(serial,"                ",items[a],"                 ",sold_quantity1[a],"              ",total_amount1[a],"              ",discounted_price1[a],"         ")
    
    elif current_salesperson==1 :
        for a in range (0 , idx1 +1) :
            serial=serial +1
            print(serial,"                ",items[a],"                 ",sold_quantity2[a],"              ",total_amount2[a],"              ",discounted_price2[a],"         ")
    elif current_salesperson==2 :
        for a in range (0 , idx1 +1) :
            serial=serial +1
            print(serial,"                ",items[a],"                 ",sold_quantity3[a],"              ",total_amount3[a],"              ",discounted_price3[a],"         ")
    elif current_salesperson==3 :
        for a in range (0 , idx1 +1) :
            serial=serial +1
            print(serial,"                ",items[a],"                 ",sold_quantity4[a],"              ",total_amount4[a],"              ",discounted_price4[a],"         ")
    elif current_salesperson==4 :
        for a in range (0 , idx1 +1) :
            serial=serial +1
            print(serial,"                ",items[a],"                 ",sold_quantity5[a],"              ",total_amount5[a],"              ",discounted_price5[a],"         ")
    press_key()

def cash_balance() :
    balance=0
    global sell_idx
    global current_salesperson
    global cash
    global discounted_price1
    global discounted_price2
    global discounted_price3
    global discounted_price4
    global discounted_price5
    q=sell_idx
    if current_salesperson==0 :
        balance=cash-discounted_price1[q]        
    elif current_salesperson==1 :
        balance=cash-discounted_price2[q]            
    elif current_salesperson==2 :
        balance=cash-discounted_price3[q]
    elif current_salesperson==3 :
        balance=cash-discounted_price4[q]
    elif current_salesperson==4 :
        balance=cash-discounted_price5[q] 
    
    return balance


def cash_balanceUI() :
    if cash_balance()>0 :
        print("PAY BACK ",cash_balance()," Rupees to customer.")
    elif cash_balance()<0 :
        print("Customer has to pay ",(-1)*cash_balance()," Rupees more.")
    press_key()

def demo_data_items() :
    add_items("shirt" , 20 , 700 , 800 , 0)
    add_items("jeans" , 10 , 2000 , 2200 , 1)
    add_items("tie" , 15 , 200 , 300 , 2)
def demo_data_salesperson() :
    add_salesperson("Fawzan" , 1111 , 0)
    add_salesperson("Arsal" , 2222 , 1)
    add_salesperson("Ahmed" , 3333 , 2)









#demo_data_items()
#demo_data_salesperson()
load_salesperson()                                          
load_items()
while True :
    os.system("cls")
    get_title()
    username=""
    password=0
    opt=0

    print(" ****Hi there,Welcome to the clothing shop****")
    print("\n")
    print("Please enter your username and password:")
    username=input("USERNAME: ")
    password=int(input("PASSWORD: "))
    if username=="Admin" and password==1234 :
        while opt!=11 :
            opt=admin_menu()
            if opt==1 :
                add_salespersonUI()
            
            elif opt==2 :
                save_salesperson()
                view_salesperson()
            elif opt==3 :
                replace_salesperson()
            elif opt==4 :
                add_itemsUI()
            elif opt==5 :
                view_items()
            elif opt==6 :
                replace_items()
            elif opt==7 :
                sort_items()
            elif opt==8 :
                total_sale_today()
            elif opt==9 :
                profit_today()
            elif opt==10 :
                discount_days()

    for x in range (0 , len(username_salesperson)) :
        if username==username_salesperson[x] and password==password_salesperson[x] :
            while opt1!=11 :
                
                current_salesperson=x
                opt1=salesperson_menu()
                if opt1==1 :
                    day_today()
                elif opt1==2 :
                    item_name()
                elif opt1==3 :
                    quantity_of_items()     
                elif opt1==4 :
                    actual_amount()
                elif opt1==5 :
                    discounted_amount()
                elif opt1==6 :
                    total_payable_amount()
                elif opt1==7 :
                    cash_received()
                elif opt1==8 :
                    cash_balanceUI()
                elif opt1==9 :
                    daily_salereport()
                elif opt1==10 :
                    view_items()
    
#MAIN FUNCTION END
