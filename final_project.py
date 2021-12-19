from datetime import datetime
member_list = [["101","Eyasin Bhuiyan",0.00,"Paid"], ["102","Sabbir Talukder",2000.0,"Unpaid"], ["103","Kaniz Fatema",2000.0,"Unpaid"],["104","Somu Saha",0.00,"Paid"], ["105","Jinnat Trisha",2000.0,"Unpaid"], ["106","Abrar Nill",2000.0,"Unpaid"], ["107","Trisha Siddiqua",0.00,"Paid"], ["108","Tonny Sarkar",2000.0,"Unpaid"], ["109","Maruf Ahmed",2000.0,"Unpaid"], ["110","Mahbubur Rahman",2000.0,"Unpaid"]]

#Today Date and Time Function
def date_time():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y  %H:%M:%S")
    print(date_time)

# Print Member list function
def print_member_list():
  print("Member List:")
  print("-------------")
  print("Member ID    Member name         Cash    Status")
  for i in range(0, len(member_list)):
    print("{0:10}  {1:18}  {2:6}   {3:2}".format(member_list[i][0], member_list[i][1], member_list[i][2], member_list[i][3]))

#Check_total_fee()
def check_total_fee():
    print("************************************************************************************")
    print("\t<---------------   IUB Students Club   ----------------->")
    print("----------------------------------------------------------------------------------")
    print(" \t\t        ****** Total Fee ****** ")
    print("************************************************************************************")
    print("\n")
    total_fee = 0
    for i in range(0, len(member_list)):
        if member_list[i][2] == 0.00:
            total_fee = total_fee + 1
    print(f"Total Fee Collected : {total_fee*2000}/-")
    date_time()

#Check member status Function
def check_status():
    print("****** IUB Students Club ******")
    print("-------------------------------")
    print("1 -> Paid Status the Member list")
    print("2 -> Unpaid Status the Member list")
    print("3 -> All the Member list")
    op = int(input("Select option: "))
    print("\n") #For new line
    if op == 3:
        print_member_list()
    else:
        print("Member ID    Member name         Cash    Status")
    for i in range(0, len(member_list)):
        if op == 1:
            if member_list[i][3] == "Paid":
                print("{0:10}  {1:18}  {2:6}   {3:2}".format(member_list[i][0], member_list[i][1], member_list[i][2], member_list[i][3]))
        elif op == 2:
            if member_list[i][3] == "Unpaid":
                print("{0:10}  {1:18}  {2:6}   {3:2}".format(member_list[i][0], member_list[i][1], member_list[i][2], member_list[i][3]))

#Payment Receipt function
def payment_receipt(name,id):
    print("************************************************************************************")
    print("|\t<---------------   IUB Students Club   ----------------->")
    print("|----------------------------------------------------------------------------------")
    print("| \t\t     ****** Payment Receipt ****** ")
    print("|----------------------------------------------------------------------------------")
    print(f"|     Mrmber ID : {id}")
    print(f"|   Member Name : {name}")
    print("|----------------------------------------------------------------------------------")
    print("| Gross Payable \t:\t\t2000\-")
    print("************************************************************************************")
    print("Status : Paid ")
    print("Thank You.")
    date_time()
    #Update Data
    for i in range(0, len(member_list)):
            if member_list[i][0] == id:
                member_list[i][2] = 0.00
                member_list[i][3] = "Paid"

# Add or Remove Member Function
def add_or_remove():
    print("****** IUB Students Club ******")
    print("-------------------------------")
    print("1 -> Add the New Member ")
    print("2 -> Remove the Member ")
    op1 = int(input("Select option: "))
    print("\n") #For new line
    if op1 == 1:
        new_id = input("Enter New Member ID : ")
        new_name = input("Enter New Member Name : ")
        new_status = input("Enter New Member Status (Paid/Unpaid): ")
        if new_status == "Paid":
            value = 0.00
            list_2 = [new_id,new_name,value,new_status]
            member_list.append(list_2)
            payment_receipt(new_name,new_id)
        else:
            value = 2000.0
            list_2 = [new_id,new_name,value,new_status]
            member_list.append(list_2)
            
        
    elif op1 == 2:
        id = input("Enter Member ID : ")
        for j in member_list:
            if j[0] == id:
                member_list.remove(j)
                print("Remove the member successful.")
                date_time() # Date and Time function call


option = 0 

while option != "0": #Exit loop when the value is 0
    print("****** IUB Students Club ******")
    print("-------------------------------")
    print("What do you wish to do?")
    print("1 -> Print the Member list")
    print("2 -> Check Total Fee")
    print("3 -> Check member status")
    print("4 -> Payment Receipt")
    print("5 -> Add or Remove Member")
    print("0 -> Exit menu")
    option = input("Select option: ")
    print("\n") #For new line
 
  #Check chosen option and call the appropriate function
    if option == "1":
    #Call the print_member_list() function
        print_member_list()
        print("\n") #For new line
    elif option == "2":
    #Call the check_total_fee() function
        check_total_fee() 
        print("\n") #For new line
    elif option == "3":
    #Call the check_status() function
        check_status() 
        print("\n") #For new line
    elif option == "4":
    #Call the payment_receipt() function
        id = input("Enter Member ID : ")
        name = input("Enter Member Name : ")
        print("\n")
        payment_receipt(name,id)
        print("\n")#For new line
    elif option == "5":
    #Call the add_or_remove() function
        add_or_remove() 
        print("\n")#For new line