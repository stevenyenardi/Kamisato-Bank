#STEVEN YENARDI
#TP062937

def transactionDate():
    import datetime as currentDate
    date = currentDate.datetime.now()
    date = date.strftime("%Y-%m-%d")
    return date

def statementOFAccountAdmin():
    # STATEMENT OF ACCOUNT REPORT
    success = False
    while not success:
        error = False
        file = open("account report.txt", "r")
        user_id = input("INPUT CUSTOMER USER ID: ")
        if user_id.lower() == 'exit':
            break
        s_date = input("Enter the starting date [YYYY-MM-DD]: ")
        e_date = input("Enter the ending date [YYYY-MM-DD]: ")
        print(f"\n{user_id} STATEMENT OF ACCOUNT REPORT\n")
        print("User ID".center(11) + "|" + "Date".center(10) + "|" + "Action".center(6) + "|" + "Amount".center(9) + "|" + "Past Balance".center(15) + "|" + "Current Balance".center(18))
        print("--------------------------------------------------------------------------")
        for rec in file:
            user = rec.split("|")
            if user_id == user[0]:
                date = user[1]
                report = user[0].ljust(11) + '|' + user[1].ljust(10) + '|' + user[2].center(6) + '|' + user[3].center(9) + '|' + user[4].center(15) + '|' + user[5].center(18)
                try:
                    if int(s_date.split("-")[0]) <= int(e_date.split("-")[0]):
                        if int(s_date.split('-')[0]) == int(date.split('-')[0]) or int(e_date.split('-')[0]) == int(date.split('-')[0]):
                            if int(s_date.split('-')[1]) <= int(e_date.split('-')[1]) and (int(s_date.split('-')[1]) < 13) and (int(e_date.split('-')[1]) < 13):
                                if int(s_date.split('-')[1]) == int(e_date.split('-')[1]) and int(e_date.split('-')[1]) == int(date.split('-')[1]):
                                    if (int(date.split('-')[2]) > int(s_date.split('-')[2])) and (int(date.split('-')[2]) < int(e_date.split('-')[2])):
                                        print(report)
                                        success = True
                                    elif (int(date.split('-')[2]) > int(s_date.split('-')[2])) and (int(e_date.split('-')[2]) == int(date.split('-')[2])):
                                        print(report)
                                        success = True
                                    elif (int(date.split('-')[2]) == int(s_date.split('-')[2])) and (int(date.split('-')[2]) < int(e_date.split('-')[2])):
                                        print(report)
                                        success = True
                                    elif (int(date.split('-')[2]) == int(s_date.split('-')[2])) and (int(e_date.split('-')[2]) == int(date.split('-')[2])):
                                        print(report)
                                        success = True
                                elif (int(s_date.split('-')[1]) < int(date.split('-')[1])) and (int(e_date.split('-')[1]) > int(date.split('-')[1])):
                                    print (report)
                                    success = True
                                elif (int(s_date.split('-')[1]) < int(date.split('-')[1])) and (int(e_date.split('-')[1]) == int(date.split('-')[1])):
                                    if (int(date.split('-')[2]) <= int(e_date.split('-')[2])):
                                        print(report)
                                        success = True
                                elif (int(s_date.split('-')[1]) == int(date.split('-')[1])) and (int(e_date.split('-')[1]) > int(date.split('-')[1])):
                                    if (int(date.split('-')[2]) >= int(e_date.split('-')[2])):
                                        print(report)
                                        success = True
                            elif (int(s_date.split('-')[0]) < int(date.split('-')[0])) or (int(e_date.split('-')[0]) > int(date.split('-')[0])):
                                print(report)
                                success = True
                except:
                    print("!!!INVALID FORMAT!!!")
                    error = True
                    break
        if not success and not error:
            print("Transactions do not exist!")
        file.close()

def blockUnblockCustomer(user, count):
    #BLOCK CUSTOMER ACCOUNT
    file = open("data.txt", "r")
    line = file.readlines()
    if user[5] == 'C':
        modify = 'B'
        line[count] = f"{user[0]}|{user[1]}|{user[2]}|{user[3]}|{user[4]}|{modify}|{user[6]}|{user[7]}"
        print("\nTHE ACCOUNT HAS BEEN BLOCKED SUCCESSFULLY\n")
    elif user[5] == 'B':
        modify = 'C'
        line[count] = f"{user[0]}|{user[1]}|{user[2]}|{user[3]}|{user[4]}|{modify}|{user[6]}|{user[7]}"
        print("\nTHE ACCOUNT HAS BEEN UNBLOCKED SUCCESSFULLY\n")
    file = open("data.txt", "w")
    file.writelines(line)
    file.close()

def readCustomerID2():
    #INPUT CUSTOMER'S USER ID BEFORE BLOCKING IT
    while True:
        user_id = input("Enter User ID: ")
        if user_id.lower() == 'exit':
            break
        fileHandle = open("data.txt","r")
        flag = 0
        count = -1
        for rec in fileHandle:
            user = rec.split('|')
            count += 1
            if user_id == user[0] and user_id[8:11] == 'CST':
                flag = 1
                break
        if flag == 1:
            blockUnblockCustomer(user, count)
            break
        else:
            print("USER ID IS NOT AVAILABLE")
        fileHandle.close()

def modifyAdminAccount(user,count):
    #SELECT ADMIN'S DATA AND MODIFY IT
    print( f"1.User ID : {user[0]}\n2.Name : {user[1]}\n3.Password : {user[2]}\n4.Phone Number: {user[3]}\n5.Date of Birth: {user[4]}\n6.EXIT")
    option = int(input("Please enter an option number that need to be changed: "))
    file = open("data.txt", "r")
    line = file.readlines()
    if option == 1:
        print("\n!!!THIS DATA CANNOT BE MODIFIED!!!\n")
    elif option == 2:
        modify = input("Enter the new name: ")
        line[count] = f"{user[0]}|{modify}|{user[2]}|{user[3]}|{user[4]}|{user[5]}|{user[6]}"
    elif option == 3:
        print("\n!!!THIS DATA CANNOT BE MODIFIED!!!\n")
    elif option == 4:
        modify = input("Enter the new phone number: ")
        line[count] = f"{user[0]}|{user[1]}|{user[2]}|{modify}|{user[4]}|{user[5]}|{user[6]}"
    elif option == 5:
        modify = input("Enter the new date of birth: ")
        line[count] = f"{user[0]}|{user[1]}|{user[2]}|{user[3]}|{modify}|{user[5]}|{user[6]}"
    elif option == 6:
        print("EXITED")
    else:
        print("!!!THIS OPTION IS NOT AVAILABLE!!!\n")
    file = open("data.txt", "w")
    file.writelines(line)
    file.close()

def readAdminID():
    #INPUT CUSTOMER'S USER ID BEFORE MODIFYING THEIR DATA
    while True:
        user_id = input("Enter User ID: ")
        if user_id.lower() == 'exit':
            break
        fileHandle = open("data.txt","r")
        flag = 0
        count = -1
        for rec in fileHandle:
            user = rec.split('|')
            count += 1
            if user_id == user[0] and user_id[8:11] == 'ADM':
                flag = 1
                break
        if flag == 1:
            modifyAdminAccount(user, count)
            break
        else:
            print("USER ID IS NOT AVAILABLE")
        fileHandle.close()

def statementOfAccountCustomer(username, name):
    # STATEMENT OF ACCOUNT REPORT
    success = False
    while not success:
        error = False
        user_id = username
        file = open("account report.txt", "r")
        s_date = input("Enter the starting date [YYYY-MM-DD]: ")
        e_date = input("Enter the ending date [YYYY-MM-DD]: ")
        print(f"\n{name} STATEMENT OF ACCOUNT REPORT\n")
        print("User ID".center(11) + "|" + "Date".center(10) + "|" + "Action".center(6) + "|" + "Amount".center(9) + "|" + "Past Balance".center(15) + "|" + "Current Balance".center(18))
        print("--------------------------------------------------------------------------")
        for rec in file:
            user = rec.split("|")
            if user_id == user[0]:
                date = user[1]
                report = user[0].ljust(11) + '|' + user[1].ljust(10) + '|' + user[2].center(6) + '|' + user[3].center(9) + '|' + user[4].center(15) + '|' + user[5].center(18)
                try:
                    if int(s_date.split("-")[0]) <= int(e_date.split("-")[0]):
                        if int(s_date.split('-')[0]) == int(date.split('-')[0]) or int(e_date.split('-')[0]) == int(date.split('-')[0]):
                            if int(s_date.split('-')[1]) <= int(e_date.split('-')[1]) and (int(s_date.split('-')[1]) < 13) and (int(e_date.split('-')[1]) < 13):
                                if int(s_date.split('-')[1]) == int(e_date.split('-')[1]) and int(e_date.split('-')[1]) == int(date.split('-')[1]):
                                    if (int(date.split('-')[2]) > int(s_date.split('-')[2])) and (int(e_date.split('-')[2]) > int(date.split('-')[2])):
                                        print(report)
                                        success = True
                                    elif (int(date.split('-')[2]) > int(s_date.split('-')[2])) and (int(e_date.split('-')[2]) == int(date.split('-')[2])):
                                        print(report)
                                        success = True
                                    elif (int(date.split('-')[2]) == int(s_date.split('-')[2])) and (int(e_date.split('-')[2]) > int(date.split('-')[2])):
                                        print(report)
                                        success = True
                                    elif (int(date.split('-')[2]) == int(s_date.split('-')[2])) and (int(e_date.split('-')[2]) == int(date.split('-')[2])):
                                        print(report)
                                        success = True
                                elif (int(s_date.split('-')[1]) < int(date.split('-')[1])) and (int(e_date.split('-')[1]) > int(date.split('-')[1])):
                                    print(report)
                                    success = True
                                elif (int(s_date.split('-')[1]) < int(date.split('-')[1])) and (int(e_date.split('-')[1]) == int(date.split('-')[1])):
                                    if (int(date.split('-')[2]) <= int(e_date.split('-')[2])):
                                        print(report)
                                        success = True
                                elif (int(s_date.split('-')[1]) == int(date.split('-')[1])) and (int(e_date.split('-')[1]) > int(date.split('-')[1])):
                                    if (int(date.split('-')[2]) >= int(e_date.split('-')[2])):
                                        print(report)
                                        success = True
                            elif (int(s_date.split('-')[0]) < int(date.split('-')[0])) or (int(e_date.split('-')[0]) > int(date.split('-')[0])):
                                print(report)
                                success = True
                except:
                    print("!!!INVALID FORMAT!!!")
                    error = True
                    break
        if not success and not error:
            print("Transactions do not exist!")
            break
        file.close()

def accountReportDeposit(amount, total, balance, user_unique_id):
    #REPORT ON DEPOSIT
    dateNow = transactionDate()
    file = open("account report.txt", "a")
    userid = f'KMST{user_unique_id}CST'
    file.write(userid.ljust(10)+"|"+dateNow.ljust(10)+"|"+"D".center(6)+"|"+ str(amount).center(9)+"|"+ str(balance).center(15)+"|"+ str(total).center(18)+'\n')
    file.close()

def accountReportWithdraw(amount, total, balance, user_unique_id):
    #REPORT ON WITHDRAWAL
    dateNow = transactionDate()
    file = open("account report.txt","a")
    userid = f'KMST{user_unique_id}CST'
    file.write(userid.ljust(10)+"|"+dateNow.ljust(10)+"|"+"W".center(6)+"|"+ str(amount).center(9)+"|"+ str(balance).center(15)+"|"+ str(total).center(18)+'\n')
    file.close()

def changePassword(username: object, useraccount: object, userpass: object, user_unique_id: object, name):
    #CHANGE CUSTOMER PASSWORD ACCOUNT
    file = open("data.txt", "r")
    cnt = -1
    for rec in file:
        user = rec.split("|")
        cnt += 1
        if username == user[0]:
            password = user[2]
            break
    while True:
        new_password = input("Enter your new password: ")
        new_password_reinput = input("Please re-enter your new password to confirm: ")
        if new_password == password:
            print("THIS IS THE SAME PASSWORD!")
        elif len(new_password) <= 6:
            print("NEW PASSWORD TOO SHORT. PLEASE INPUT AT LEAST 7 CHARACTERS")
        elif new_password != new_password_reinput:
            print("YOU HAVE A MISTAKE ON RE-INPUTING YOUR NEW PASSWORD")
        else:
            break
    while True:
        confirmation = str(input("Are you sure you want to change your password? [Y/N]: "))
        if confirmation.upper() == 'Y':
            file = open("data.txt", "r")
            line = file.readlines()
            line[cnt] = f"{user[0]}|{user[1]}|{new_password}|{user[3]}|{user[4]}|{user[5]}|{user[6]}|{user[7]}"
            file = open("data.txt", "w")
            file.writelines(line)
            file.close()
            print("\nPASSWORD CHANGED\n")
            break
        elif confirmation.upper() == 'N':
            break
        else:
            print('\nThis option is not available\n')
    file.close()

def withdraw(username, useraccount, userpass, user_unique_id, name):
    #WITHDRAW SYSTEM
    file = open("data.txt", "r")
    cnt = -1
    for rec in file:
        user = rec.split("|")
        cnt += 1
        if username == user[0]:
            balance = float(user[7])
            break
    file.close()

    while True:
        try:
            while True:
                amount = float(input("Please input the amount: "))
                confirmation = str(input(f'Are you sure to withdraw RM {amount} from your account?[Y/N]: '))
                if confirmation.upper() == "Y":
                    total = float(balance) - amount
                    if useraccount == "Cu" and total < 500:
                        print("\nAFTER THE WITHDRAWAL, YOUR BALANCE IS UNDER THE MINIMUM BALANCE LIMIT\n")
                    elif useraccount == "Sa" and total < 100:
                        print("\nAFTER THE WITHDRAWAL, YOUR BALANCE IS UNDER THE MINIMUM BALANCE LIMIT\n")
                    else:
                        file = open("data.txt", "r")
                        line = file.readlines()
                        line[cnt] = f"{user[0]}|{user[1]}|{user[2]}|{user[3]}|{user[4]}|{user[5]}|{user[6]}|{total}\n"
                        file = open("data.txt", "w")
                        file.writelines(line)
                        file.close()
                        print("\nWITHDRAW SUCCESSFUL\n")
                        accountReportWithdraw(amount, total, balance, user_unique_id)
                        break
                elif confirmation.upper() == 'N':
                    break
                else:
                    print('\nThis option is not available\n')
            break
        except:
            print("!!!INVALID INPUT!!!")

def deposit(username, useraccount, userpass, user_unique_id, name):
    #DEPOSIT SYSTEM
    file = open("data.txt", "r")
    cnt = -1
    for rec in file:
        user = rec.split("|")
        cnt += 1
        if username == user[0]:
            balance = float(user[7])
            break
    file.close()

    while True:
        try:
            while True:
                amount = float(input("Please input the amount: "))
                confirmation = str(input(f'Are you sure to deposit RM {amount} from your account?[Y/N]: '))
                if confirmation.upper() == 'Y':
                    total = float(balance) + amount
                    file = open("data.txt", "r")
                    line = file.readlines()
                    line[cnt] = f"{user[0]}|{user[1]}|{user[2]}|{user[3]}|{user[4]}|{user[5]}|{user[6]}|{total}\n"
                    file = open("data.txt","w")
                    file.writelines(line)
                    file.close()
                    print("\nDEPOSIT SUCCESSFUL\n")
                    accountReportDeposit(amount, total, balance, user_unique_id)
                    break
                elif confirmation.upper() == 'N':
                    break
                else:
                     print('\nThis option is not available\n')
            break
        except:
            print("!!!INVALID INPUT!!!")

def checkBalance(username):
    #SHOW CURRENT BALANCE WHEN CUSTOMER LOGS IN
    file = open("data.txt","r")
    for rec in file:
        user = rec.split("|")
        if username == user[0]:
            balance = user[7]
            break
    print(f"Account Balance = RM {balance}")
    file.close()

def customerAccount(username, useraccount, userpass, user_unique_id, name):
    #CUSTOMER ACCOUNT OPTION
    option = ''
    while option != 5 :
        user = name
        print(f'Welcome {user}!')
        print("-" * 25)
        checkBalance(username)
        file = open("data.txt", "r")
        print("\n1.DEPOSIT\n2.WITHDRAW\n3.CHANGE PASSWORD\n4.STATEMENT OF ACCOUNT REPORT\n5.EXIT\n")
        try:
            option = int(input("Please enter an option's number: "))
            if option == 1:
                # DEPOSIT SYSTEM
                deposit(username, useraccount, userpass, user_unique_id, name)
            elif option == 2:
                # WITHDRAW SYSTEM
                withdraw(username, useraccount, userpass, user_unique_id, name)
            elif option == 3:
                # CHANGE CUSTOMER'S PASSWORD
                changePassword(username, useraccount, userpass, user_unique_id, name)
            elif option == 4:
                # STATEMENT OF ACCOUNT REPORT
                statementOfAccountCustomer(username, name)
            elif option == 5:
                # EXIT
                print("See you next time!")
                break
            else:
                print("!!!THIS OPTION IS NOT AVAILABLE!!!")
            file.close()
        except:
            print("!!!INVALID INPUT!!!")


def modifyCustomerData(user, count):
    #CHANGE CUSTOMER DATA
        print(f"1.User ID : {user[0]}\n2.Name : {user[1]}\n3.Phone Number : {user[3]}\n4.Date of Birth: {user[4]}\n5.Type of Account: {user[6]}\n6.EXIT")
        option = int(input("Please enter an option number that need to be changed: "))
        file = open("data.txt","r")
        line = file.readlines()
        if option == 1:
            print("!!!THIS DATA CANNOT BE MODIFIED!!!\n")
        elif option == 2:
            print("!!!THIS DATA CANNOT BE MODIFIED!!!\n")
        elif option == 3:
            modify = input("Enter the new phone number: ")
            line[count] = f"{user[0]}|{user[1]}|{user[2]}|{modify}|{user[4]}|{user[5]}|{user[6]}|{user[7]}"
        elif option == 4:
            modify = input("Enter the new date of birth: ")
            line[count] = f"{user[0]}|{user[1]}|{user[2]}|{user[3]}|{modify}|{user[5]}|{user[6]}|{user[7]}"
        elif option == 5:
            print("!!!THIS DATA CANNOT BE MODIFIED!!!\n")
        elif option == 6:
            print("EXITED")
        else:
            print("!!!THIS OPTION IS NOT AVAILABLE!!!\n")
        file = open("data.txt","w")
        file.writelines(line)
        file.close()

def readCustomerId():
    #INPUT CUSTOMER ID BEFORE CHANGING THE DATA
    while True:
        user_id = input("Enter User ID: ")
        if user_id.lower() == 'exit':
            break
        fileHandle = open("data.txt","r")
        flag = 0
        count = -1
        for rec in fileHandle:
            user = rec.split('|')
            count += 1
            if user_id == user[0] and user_id[8:11] == 'CST':
                flag = 1
                break
        if flag == 1:
            modifyCustomerData(user, count)
            break
        else:
            print("USER ID IS NOT AVAILABLE")
        fileHandle.close()

def username_id():
    #CREATE ADMIN ACCOUNT ID
    file = open("data.txt","r")
    for rec in file:
        user = rec.split("|")
        user_id = user[0]
        user_unique_id = int(user_id[4:8])
        user_unique_id += 1
    file.close()

    file = open("data.txt","a")
    file.write("KMST" + str(user_unique_id) + "ADM" + "|")
    file.close()

def cstusername_id():
    #CREATE CUSTOMER ACCOUNT ID
    file = open("data.txt", "r")
    for rec in file:
        user = rec.split("|")
        user_id = user[0]
        user_unique_id = int(user_id[4:8])
        user_unique_id += 1
    file.close()

    file = open("data.txt", "a")
    file.write("KMST" + str(user_unique_id) + "CST" + "|")
    file.close()

def newAdminAccount():
    #CREATE NEW ADMIN ACCOUNT
    full_name = str(input("Name: "))
    phone_number = int(input("Phone Number:"))
    birth_date = input("Birth date [DD/MM/YY]: ")

    file = open("data.txt", "a")
    username_id()
    file.write(full_name + "|")
    file.write("KMSTadmin" + "|")
    file.write(str(phone_number) + "|")
    file.write(str(birth_date) + "|")
    file.write(str("A") + "|" + "\n")
    file.close()

    file = open("data.txt", "r")
    line = file.readline()
    line = line.split("|")
    file.close()
    print("\nADMIN ACCOUNT IS SUCCESSFULLY CREATED\n")

def superAccount(name):
    #SUPER ACCOUNT OPTION
    option = ''
    while option != 5:
        print(f"Welcome {name}!")
        print("-"*25)
        print("\n1.CREATE NEW ADMIN ACCOUNT\n2.CHECK & MODIFY ADMIN ACCOUNT\n3.CHECK & MODIFY CUSTOMER ACCOUNT\n4.BLOCK OR UNBLOCK CUSTOMER ACCOUNT\n5.EXIT\n")
        try:
            option = int(input("Please enter an option's number: "))
            if option == 1:
                # CREATE NEW ADMIN ACCOUNT
                newAdminAccount()

            elif option == 2:
                # TO LOOK AT ADMIN'S DATA AND MODIFY IT
                readAdminID()

            elif option == 3:
                # TO LOOK AT CUSTOMER'S DATA AND MODIFY IT
                readCustomerId()

            elif option == 4:
                # BLOCK CUSTOMER'S ACCOUNT
                readCustomerID2()

            elif option == 5:
                # EXIT
                print("See you next time!")
                break

            else:
                # WHEN USER ENTERED AN OPTION THAT IS NOT AVAILABLE
                print("\n!!!THIS OPTION IS NOT AVAILABLE!!!\n")

        except:
            print("!!!INVALID INPUT!!!")

def newCustomerAccount():
    #CREATE NEW CUSTOMER ACCOUNT
    first_name = str(input("First name:"))
    last_name = str(input("Last name:"))
    phone_number = int(input("Phone Number:"))
    birth_date = input("Birth date [DD/MM/YY]: ")
    customer_type = ''
    while customer_type != 'Cu' or customer_type != "Sa":
        customer_type = str(input("Account type[Cu/Sa]: "))
        if customer_type == 'Cu':
            break
        elif customer_type == 'Sa':
            break
        else:
            print("!!!THIS TYPE OF ACCOUNT IS NOT AVAILABLE!!!")

    file = open("data.txt", "a")
    cstusername_id()
    file.write(str(first_name) + ' ' + str(last_name) + "|")
    file.write("KMST" + str(first_name) + str(last_name) + "|")
    file.write(str(phone_number) + "|")
    file.write(str(birth_date) + "|")
    file.write(str("C") + "|")
    file.write(str(customer_type) + "|")
    if customer_type == 'Cu':
        file.write("500" + "\n")
    elif customer_type == 'Sa':
        file.write("100" + "\n")
    file.close()

    file = open("data.txt", "r")
    line = file.readline()
    line = line.split("|")
    file.close()
    print("CUSTOMER ACCOUNT IS SUCCESSFULLY CREATED")

def adminAccount(name):
    #ADMIN ACCOUNT OPTION
    option = ''
    while option != 4:
        print(f'Welcome {name}!')
        print("-"*25)
        print("\n1.CREATE NEW CUSTOMER DATA\n2.EDIT CUSTOMER DATA\n3.STATEMENT OF ACCOUNT REPORT\n4.EXIT\n")
        try:
            option = int(input("Please enter an option's number: "))
            if option == 1:
                #CREATE NEW CUSTOMER ACCOUNT
                newCustomerAccount()

            elif option == 2:
                #EDIT CUSTOMER DATA
                readCustomerId()

            elif option == 3:
                #STATEMENT OF ACCOUNT REPORT
                statementOFAccountAdmin()

            elif option == 4:
                #EXIT
                print("See you next time!")
                break

            else:
                print("!!!THIS OPTION IS NOT AVAILABLE!!!\n")

        except:
            print("!!!INVALID INPUT!!!")

def login():
    #LOGIN MENU
    print("Welcome to Kamisato Bank")
    while True:
            file = open("data.txt", "r")
            username = input("Username : ")
            password = input("Password : ")
            success = False
            for rec in file:
                user = rec.split("|")
                if username == user[0] and password == user[2]:
                    success = True
                    name = user[1]
                    userpass = user[2]
                    usertype = user[5]
                    useraccount = user[6]
                    user_unique_id = int(username[4:8])
                    break
            file.close()

            if success == True:
                print("\nLogin Successful!\n")
                if usertype == "S":
                    superAccount(name)
                    break
                elif usertype == "A":
                    adminAccount(name)
                    break
                elif usertype == "C":
                    customerAccount(username, useraccount, userpass, user_unique_id, name)
                    break
                elif usertype == "B":
                    print("\n!!!THIS ACCOUNT HAS BEEN BLOCKED!!!\n")
                    break
            else:
                print("\nLogin Unsuccessful. Please try again!\n")

login()