import json
import os
import time,datetime


#function to clear screen
def clear():
    os.system("cls")


#function to select whether ur Customer or Admin

def main():

    clear()
    while True:
        print("\n\t\t\t\t\tENTER A CHOICE \n\n\t1.Admin\t\t2.Customer\t\t3.Exit")
        try:
            CHOICE = int(input("\nEnter your choice:"))
        except:
            print("\nOnly Integer value!! Please Re-enter")
            continue
        if CHOICE == 1:
            admin()

        elif CHOICE == 2:
            customer()

        elif CHOICE == 3:
            break

        else :
            print("\n Invalid Choice!! Please try again")



#function to select various options that could be performed by admin using the inventory

def admin():

    clear()
    while True:
        print("\n\t\t\t\t\t\t\t\t\t\tENTER A CHOICE \n\n\t1.Add Products\t\t2.Remove Products\t\t3.Update the Existing Products\t\t4.Display the Inventory\t\t5.Display the Products sold\t\t6.Exit")
        try:
            CHOICE = int(input("\nEnter your choice:"))
        except:
            print("\nOnly Integer value!! Please Re-enter")
            continue
        if CHOICE == 1:
            addinventory()

        elif CHOICE == 2:
            removinventory()

        elif CHOICE == 3:
            updatekey()

        elif CHOICE == 4:
            displayinventory()

        elif CHOICE == 5:
            displaysales()

        elif CHOICE == 6:
            break

        else :
            print("\n Invalid Choice!! Please try again")
    clear()



#function to select various options that could be performed by customer using the inventory

def customer():

    clear()
    while True:
        print("\n\t\t\t\t\tENTER A CHOICE \n\n\t1.Display the Inventory\t\t2.Purchase Product/Products\t\t3.Exit")
        try:
            CHOICE = int(input("\nEnter your choice:"))
        except:
            print("\nOnly Integer value!! Please Re-enter")
            continue
        if CHOICE == 1:
            displayinventory()

        elif CHOICE == 2:
            purchase()

        elif CHOICE == 3:
            break

        else :
            print("\n Invalid Choice!! Please try again")

    clear()


#function to verify and get the correct quantity and price of the product
def get_quantity_price(flag):

    if flag ==1:
        while True:
            try:
                quantity = int(input("\nEnter the quantity: "))
            except:
                print("\nEnter a whole number")
                continue
            if quantity<=-1:
                print("\nPlease Re-enter!!Quantity cannot be negative")
            else:
                break
        return quantity
    else:
          while True:
            try:
                price = int(input("\nEnter the price per piece:"))
            except:
                print("\nEnter a whole number")
                continue
            if price<=0:
                print("\nPrice of product cannot be zero or a negative value!! Please Re-enter a positive value")
            else:
                break
    return price

#Function to validate dates entered by user

def dates():

    date = input("\nEnter the date in dd/mm/yyyy format: ")
    day,month,year = date.split('/')
    day = int(day)
    month = int(month)
    year = int(year)

    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        max_days = 31
    elif month==4 or month==6 or month==9 or month==11:
        max_days = 30
    elif year%4==0 and year%100!=0 or year%400==0:
        max_days = 29
    else:
        max_days = 28

    if month<1 or month>12 or day<1 or day>max_days:
        print("\nEntered date is Invalid!!\n Please Try again")
        dates()

    return date



#function to check expiry daye > manufacturing date

def check_date( date1 , date2 ):

    day1,month1,year1 = date1.split('/')
    day1 = int(day1)
    month1 = int(month1)
    year1 = int(year1)

    day2,month2,year2 = date2.split('/')
    day2 = int(day2)
    month2 = int(month2)
    year2 = int(year2)

    if year2>year1:
        return 1
    elif year2==year1 and month2>month1:
        return 1
    elif year2==year1 and month2==month1 and day2>day1:
        return 1
    else:
        print("\nExpiry date cannot be less than Manufacturing Date Please Re-enter the date!!")
        return 0


#Function to add items to the inventory
def addinventory():

    clear()
    record = {}
    InventoryFile = open('Record.json', 'r')
    jdata = InventoryFile.read()
    record = json.loads(jdata)
    InventoryFile.close()
    while True:
        clear()
        try:
            key = int(input("\nEnter the product code: "))
            key=str(key)
        except:
            print("\nEnter a whole number")
            continue

        name = input("\nEnter the product name: ")
        quantity = get_quantity_price(1)
        price = get_quantity_price(0)

        flag=0

        while flag!=1:
            print("\nEnter Date of Manufacture: ")
            dom = dates()
            print("\nEnter Expiry date: ")
            ed = dates()
            flag = check_date( dom , ed )


        record[key] = { 'Name' : name , 'Quantity' : quantity , 'Price' : price , 'Manufacturing Date' : dom , 'Expiry Date' : ed}

        InventoryFile = open('Record.json', 'r+')
        jdata = json.dumps(record)
        InventoryFile.writelines(jdata)
        InventoryFile.close()

        print("\nEnter y to add more items and n to stop adding: ")
        if option()=='y':
            continue
        else:
            break

    prev = input("\n\n \t\t\t\t\tPress Enter to continue:")
    clear()


#Remove an item from the Inventory
def removinventory():

    clear()
    InventoryFile = open('Record.json', 'r')
    jdata = InventoryFile.read()
    record = json.loads(jdata)
    InventoryFile.close()
    while True:
        key = input("Enter the product Key to be removed: ")
        if key in record.keys():
            del record[key]
            InventoryFile = open('Record.json', 'w')
            jdata = json.dumps(record)
            InventoryFile.write(jdata)
            InventoryFile.close()
            print("\n Product Removed Successfully!!")
        else:
            print("Invalid product Key!!")

        print("Enter y to remove an items and n to stop removing: ")

        if option()=='y':
            continue
        else :
            break

    prev = input("\n\n \t\t\t\t\tPress Enter to continue:")
    clear()



#Function to get Product code to update details of an item in the Inventory

def updatekey():

    clear()
    InventoryFile = open('Record.json', 'r')
    jdata = InventoryFile.read()
    record = json.loads(jdata)
    InventoryFile.close()

    while True:

        key = input("\nEnter the product Key to be updated: ")

        if key in record.keys():
            updateinventory(key)
        else:
            print("\nInvalid product Key!!")

        print("\nEnter y to update more products and n to stop updation: ")

        if option()=='y':
            continue
        else:
            break

    prev = input("\n\n \t\t\t\t\tPress Enter to continue:")
    clear()



#function to update details of a specific product entered by the user

def updateinventory(key):

    InventoryFile = open('Record.json', 'r')
    jdata = InventoryFile.read()
    record = json.loads(jdata)
    InventoryFile.close()

    while(1):

        more_input= 'y'

        while True :

            print("\n\t\t\t\t\t\t\t\t\t\tENTER A CHOICE \n\n\t1.Update product name\t\t2.Update product quantity\t\t3.Update product price\t\t4.Update product Date of Manufacture\t\t5.Update product Expiry Date")
            while True:
                try:
                    CHOICE=int(input("\nPlease enter an option: "))
                    break
                except:
                    print("\nInvalid Option!! Please Re-enter")
                    continue

            if CHOICE == 1:
                name=str(input("\nEnter the product name: "))
                record[key]['Name']=name
                print("\nUpdated Successfully!!")

            elif CHOICE == 2:
                print("\n\t\t\t\t\tENTER A CHOICE \n\n\t1.Add quantity\t\t2.Subtract quantity\t\t3.Put number of quantities to zero")
                while True:
                    try:
                        CHOICE=int(input("\nPlease enter an option: "))
                    except:
                        print("\nInvalid Option!! Please Re-enter")
                        continue

                    quantity = int(input("\nEnter the quantity: "))
                    if CHOICE == 1 :
                        record[key]['Quantity'] += quantity
                        print("\nUpdated Successfully!!")
                        break
                    elif CHOICE == 2 and record[key]['Quantity'] - quantity>=0:
                        record[key]['Quantity'] -= quantity
                        print("\nUpdated Successfully!!")
                        break
                    elif CHOICE == 2 and record[key]['Quantity'] - quantity<=-1:
                        continue
                    elif CHOICE == 3 :
                        record[key]['Quantity'] = 0
                        print("\nUpdated Successfully!!")
                        break
                    else :
                        print("\nInvalid Option!! Please Re-enter")

            elif CHOICE == 3:
                while True:
                    try:
                        price = int(input("\nEnter the price per piece:"))
                    except:
                        print("\nOnly Integer value!! Please Re-enter")
                        continue
                    record[key]['Price'] = price
                    print("\nUpdated Successfully!!")
                    break

            elif CHOICE == 4 or CHOICE == 5:
                flag=0
                while flag!=1:
                    print("\nEnter the new Date: ")
                    if CHOICE == 4:
                        md = dates()
                        record[key]['Manufacture Date'] = md
                        ed = record[key]['Expiry Date']
                    elif CHOICE == 5:
                        ed = dates()
                        record[key]['Expiry Date'] = ed
                        md = record[key]['Manufacture Date']
                    flag = check_date( md , ed )
                    print("\nUpdated Successfully!!")

            else:
                print("\nInvalid Option!!")
                print("Please try again")

            print("\nEnter y to update more details of the same item and n to stop updating the same item: ")

            if option()=='y':
                continue
            else:
                break
        break

    InventoryFile = open('Record.json', 'w')
    jdata = json.dumps(record)
    InventoryFile.writelines(jdata)
    InventoryFile.close()

    clear()



#function to display available products with details in the Inventory
def displayinventory():

    clear()
    record = {}
    InventoryFile = open('Record.json', 'r')
    jdata = InventoryFile.read()
    record = json.loads(jdata)

    print('\t\t\t\t==============================================================================================================================================')
    print('\t\t\t\t\t\t\t\t\t\tInventory Available')
    print('\t\t\t\t==============================================================================================================================================')
    print("--Product Code--\t---Name---\t\t\t\t ---Quantity---\t\t\t---Price---\t\t\t---Manufacturing Date---\t\t\t---Expiry Date---")

    for key in record.keys():
        print(key,"\t\t\t",record[key]['Name'],"\t\t\t\t\t",record[key]['Quantity'],"\t\t\t\t",record[key]['Price'],"\t\t\t\t",record[key]['Manufacturing Date'],"\t\t\t\t\t",record[key]['Expiry Date'])

    prev = input("\n\n \t\t\t\t\tPress Enter to continue:")
    clear()
    InventoryFile.close()


#function to display sold products and its details

def displaysales():

    clear()
    sale = {}
    SalesFile = open('Sales.json', 'r')
    jdata = SalesFile.read()
    sale = json.loads(jdata)

    print('==============================================================================================================================================')
    print('\t\t\t\t\t\tSales Record')
    print('==============================================================================================================================================\n')
    for key in sale.keys() :
        print("Transaction ID : " , key , "\tName : " , sale[key]['Customer Name'] , "\tMobile Number : " , sale[key]['Contact Number'] , "\tDate : " , sale[key]['Date'] , "\tTime : " , sale[key]['Time'])
        print("Product Code\t\t\t\t Product Name\t\t\t\t Quantity\t\t\t\t Price")
        count = int(len(sale[key]))
        count = int((count-5)/4)
        for i in range(count):
            print(sale[key]['Product Code'+ str(i+1)],'\t\t\t\t\t',sale[key]['Name'+ str(i+1)],"\t\t\t\t\t",sale[key]['Quantity'+ str(i+1)],"\t\t\t\t\t",sale[key]['Price'+ str(i+1)])
        if 'Discount' in sale[key] :
            print("\nDiscount:\t" ,sale[key]['Discount'])
        print("\nTotal Amount:\t" ,sale[key]['Total'])
        print('==============================================================================================================================================\n')

    prev = input("\n\n \t\t\t\t\tPress Enter to continue:")
    clear()
    SalesFile.close()



#function to the check user choice and return accordingly

def option():
    more_input = 'y'
    while more_input!='n' :
        more_input = input()
        if more_input == 'y':
            return 'y'
        elif more_input == 'n':
            return 'n'
        else:
            print("Invalid Input!!")
            print("Please try again")


#Function to purchase items available in the inventory by the customer

def purchase():

    clear()
    InventoryFile = open('Record.json', 'r')
    jdata = InventoryFile.read()
    record = json.loads(jdata)
    InventoryFile.close()
    buy = {}

    more_purchase='y'
    while more_purchase!='n' :

        key = input("\nEnter the product code: ")

        if key in record.keys() :

            while True :
                quantity = get_quantity_price(1)

                if quantity>record[key]['Quantity'] :
                    print("\nSorry we do not that much quantity available!!")
                    counter = 'y'
                    while counter != 'n' :
                        counter = input("\nEnter y if you still want to buy a lesser quantity and n if you dont want to buy the product : ")
                        if counter == 'y' or counter == 'n' :
                            break
                        else:
                            print("Invalid Input!!")
                            print("Please try again")
                            continue

                    if counter == 'y' :
                        continue
                    else :
                        break

                else:
                    buy[key] = { 'Name' : record[key]['Name'] , 'Quantity' : quantity , 'Price' : quantity*record[key]['Price']}
                    record[key]['Quantity'] = record[key]['Quantity']-quantity
                    break
        else:
            print("\nSuch product does not exists in the inventory")
        print("\nEnter y if you want to buy more products and n if you dont want to buy more products : ")
        more_purchase=option()
        if more_purchase=='y' :
            continue
        else:
            break
    sales(buy)
    InventoryFile = open('Record.json', 'w')
    jdata = json.dumps(record)
    InventoryFile.writelines(jdata)
    InventoryFile.close()

    prev = input("\n\n \t\t\t\t\tPress Enter to continue:")
    clear()








# function that gives name to the key after the Transaction id to access the sales record

def get_sales_details(n):
    list = []
    for i in range(n):
        list.append('Product Code' + str(i+1))
        list.append('Name' + str(i+1))
        list.append('Quantity' + str(i+1))
        list.append('Price' + str(i+1))

    return list


# Function that prints bill and add to sales.json

def sales(buy):

    sale = {}
    SalesFile = open('Sales.json', 'r')
    jdata = SalesFile.read()
    sale = json.loads(jdata)
    SalesFile.close()

    total = 0
    for key in buy.keys() :
        total+=buy[key]['Price']
    discount = 0
    if total>10000:
        discount = 1000
        total -= discount
    elif total>5000:
        discount = 500
        total -= discount

    while True:
        urname=input("\nPlease Enter Your Name : ")
        if(urname.isalpha()):
            break
        elif all(x.isalpha() or x.isspace() for x in urname):
            break
        else:
            print("\nYour name cannot contain Special characters or Numbers!! Please try again")


    while True:
        try:
            number = int(input("\nEnter contact number:"))
        except:
            print("\nEnter a correct contact number")
            continue
        if number<=0:
            print("Contact cannot be zero or  negative!! Please Re-enter")
        else:
            break





    trans_no = len(sale)+1
    list_buy = []
    date = datetime.date.today().strftime('%d/%m/%Y')
    time = datetime.datetime.now().strftime('%H:%M:%S')

    for key in buy.keys() :
        list_buy.append(key)
        list_buy.append(buy[key]['Name'])
        list_buy.append(buy[key]['Quantity'])
        list_buy.append(buy[key]['Price'])
    list_buy.append(urname)
    list_buy.append(number)
    list_buy.append(date)
    list_buy.append(time)
    list_buy.append(total)
    if discount>0:
        list_buy.append(discount)


    list_no = get_sales_details(int(len(buy)))
    list_no.append('Customer Name')
    list_no.append('Contact Number')
    list_no.append('Date')
    list_no.append('Time')
    list_no.append('Total')
    if discount>0:
        list_no.append('Discount')


    bill = {}
    bill[trans_no]=dict(zip(list_no,list_buy))
    sale.update(bill)
    SalesFile = open('Sales.json','w')
    jdata = json.dumps(sale)
    SalesFile.write(jdata)
    SalesFile.close()
    clear()
    for key in bill.keys() :
        print('==============================================================================================================================================')
        print('\t\t\t\t\t\t\tYOUR BILL:')
        print('==============================================================================================================================================')
        print("Transaction ID : " , key , "\tName : " , bill[key]['Customer Name'] , "\tMobile Number : " , bill[key]['Contact Number'] , "\tDate : " , bill[key]['Date'] , "\tTime : " , bill[key]['Time'])
        print('==============================================================================================================================================')
        print("Product Code\t\t\t\t Product Name\t\t\t\t Quantity\t\t\t\t Price")
        count = int(len(bill[key]))
        count = int((count-5)/4)
        for i in range(count):
            print(bill[key]['Product Code'+ str(i+1)],'\t\t\t\t\t',bill[key]['Name'+ str(i+1)],"\t\t\t\t\t",bill[key]['Quantity'+ str(i+1)],"\t\t\t\t\t",bill[key]['Price'+ str(i+1)])
        if 'Discount' in bill[key] :
            print("\nDiscount:\t" ,bill[key]['Discount'])
        print("\nTotal Amount:\t" ,bill[key]['Total'])

        



main()
