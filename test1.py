member_list = [["101","Eyasin Bhuiyan",0.00,"Paid"], ["102","Sabbir Talukder",2000.0,"Unpaid"], ["103","Kaniz Fatema",2000.0,"Unpaid"],["104","Somu Saha",0.00,"Paid"], ["105","Jinnat Trisha",2000.0,"Unpaid"], ["106","Abrar Nill",2000.0,"Unpaid"], ["107","Trisha Siddiqua",0.00,"Paid"], ["108","Tonny Sarkar",2000.0,"Unpaid"], ["109","Maruf Ahmed",2000.0,"Unpaid"], ["110","Mahbubur Rahman",2000.0,"Unpaid"]]

# def print_member_list():
#   print("Member List:")
#   print("-------------")
#   print("Member ID    Member name         Cash    Status")
#   for i in range(0, len(member_list)):
#     print("{0:10}  {1:18}  {2:6}   {3:2}".format(member_list[i][0], member_list[i][1], member_list[i][2], member_list[i][3]))

# def add_or_remove():
#     print("****** IUB Students Club ******")
#     print("-------------------------------")
#     print("1 -> Add the New Member ")
#     print("2 -> Remove the Member ")
#     op1 = int(input("Select option: "))
    # print("\n") #For new line
    # if op1 == 1:
    #     new_id = input("Enter New Member ID : ")
    #     new_name = input("Enter New Member Name : ")
    #     new_status = input("Enter New Member Status (Paid/Unpaid): ")
    #     if new_status == "Paid":
    #         value = 0.00
    #         member_list.extend([new_id,new_name,value,new_status])
    #     else:
    #         value = 2000.0
    #         member_list.extend([new_id,new_name,value,new_status])

# add_or_remove()
# print_member_list()

new_id = input("Enter New Member ID : ")
new_name = input("Enter New Member Name : ")
new_status = input("Enter New Member Status (Paid/Unpaid): ")
value = 0.00
list_2 = [new_id,new_name,value,new_status]
member_list.append(list_2)
print(member_list)
# print(list_2)