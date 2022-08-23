import csv


class Admin:
    def __init__(self, is_admin, account_no, pin, first_name, last_name, father_name, dob,
                 gender, email, age, id_card, user_data, amount, status):
        self.is_admin = is_admin
        self.pin = pin
        self.account_no = account_no
        self.first_name = first_name
        self.last_name = last_name
        self.father_name = father_name
        self.dob = dob
        self.gender = gender
        self.email = email
        self.age = age
        self.id_card = id_card
        self.user_data = user_data
        self.amount = amount
        self.status = "active"

    def admin_login(self):
        filename = "user_data.csv"
        print("\t please Enter Admin Credentials")
        admin_card = input("\t Type ID card number without '-' ")
        print("\t Enter Account Pin")
        admin_pin = input("\t pin")

        with open(filename, newline='') as f:
            reader = csv.reader(f)
            for rows in reader:
                if admin_card == rows[-4]:
                    print(admin_card)
                    if rows[0] == "yes":
                        print("\tWelcome Admin\n")
                        if admin_pin == rows[2]:
                            print("\tYou are logged In: \n")
                            self.admin_tasks(self)

    # for username and password check if the coloumn of isAdmin True login to admin otherwise return invalid user
    def admin_tasks(self):
        print("\n---Admin portal---\n")
        print("1. Create Account\n")
        print("2. Delete Account\n")
        print("3. Update Account Information\n")
        print("4. Check User Details\n")
        print("5. Create Admin\n")

        task_selected = int(input("Enter: \t"))
        if task_selected == 1:
            Admin.create_account(self)
        elif task_selected == 2:
            Admin.delete_account(self)
        elif task_selected == 3:
            Admin.update_account(self)
        elif task_selected == 4:
            Admin.check_user_data(self)
        elif task_selected == 5:
            pass
            # CreateAdmin

    def create_account(self):
        print("---Create Account---\n")
        self.is_admin = input("for admin enter A")
        self.account_no = input("Enter Account no in digit:\t ")
        self.pin = input("Set pin in digits:\t ")
        self.first_name = input("Enter first name:\t ")
        self.last_name = input("Enter last name:\t ")
        self.father_name = input("Enter father name:\t ")
        self.email = input("Enter email:\t ")
        self.age = input("Enter age:\t ")
        self.dob = input("Enter dob in dd-mm-yyyy:\t ")
        self.gender = input("Enter M for Male or F for Female:\t ")
        self.id_card = input("Enter id card number without dash '-':\t ")
        self.amount = input("Enter initial amount to deposit:\t ")

        self.user_data = {'Admin': self.is_admin, 'Account Number': self.account_no, 'pin': self.pin,
                          'first name': self.first_name,
                          'last name': self.last_name, 'father name': self.father_name, 'email': self.email,
                          'age': self.age, 'dob in dd-mm-yyyy': self.dob, 'id_card': self.id_card,
                          "gender": self.gender, 'Amount': self.amount, 'status': self.status}

        # open csv file
        with open('user_data.csv', 'a', newline='') as self.userinfo:
            header = ['Admin', 'Account Number', 'pin', 'first name', 'last name', 'father name', 'email', 'age',
                      'dob in dd-mm-yyyy',
                      'id_card', 'gender', 'Amount', 'status']
            send_data_to_userinfo = csv.DictWriter(self.userinfo, fieldnames=header)
            # to write header.
            send_data_to_userinfo.writeheader()
            send_data_to_userinfo.writerow(self.user_data)
            print(f"\n user {self.first_name} has been added")

    def delete_account(self):
        print("Enter id_card number to delete account")
        id_card = str(input("id_card=\t"))
        status = "active"
        filename = "user_data.csv"
        fields = []
        rows = []
        self.change_status = []
        header = ['Admin', 'Account Number', 'pin', 'first name', 'last name', 'father name', 'email', 'age',
                  'dob in dd-mm-yyyy',
                  'id_card', 'gender', 'Amount', 'status']
        with open(filename, 'r') as self.customerfile:
            csvreader = csv.reader(self.customerfile)
            fields = next(csvreader)
            # for row in csvreader:
            #     rows.append(row)
            # printing first 5 rows
            print('\nFirst 5 rows are: \n')
            for rows in csvreader:
                if id_card == rows[-4]:
                    print(fields)
                    if rows[-1] == status:
                        print("this user is active")

                        with open(filename, newline='') as f:
                            reader = csv.reader(f)
                            data = list(reader)
                            for i in data:
                                if i[-4] == id_card:
                                    if i[12] == "active":
                                        i[12] = "inactive"
                                        print(f"Assets in Account  {id_card} has been frozen ")
                                        with open(filename, "w", newline='') as fw:
                                            fwriter = csv.writer(fw)
                                            fwriter.writerows(data)
                                        print(f"{id_card} data status changed to {i[12]} ")
                                        break
                                    break
                        break

                    elif rows[-1] == "inactive":
                        print("user account is frozen already")
                        print("status unchanged")
                        break
                # self.change_status.append(rows)
                # print(rows)
                # print(f"{id_card} is successfully deactivated")
                break
            else:
                print(f"user does not exist with {id_card} id card")

                # with open(filename, "a", newline='') as fw:
                #     fwriter = csv.writer(fw)
                #     fwriter.writerows(self.change_status)
                # print("status changed successfully ")

                #

                print("\n")

    def check_user_data(self):
        print("entered in check user data")
        filename = "user_data.csv"
        fields = []
        rows = []
        with open(filename, 'r') as self.customerfile:
            csvreader = csv.reader(self.customerfile)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
            # total no of rows
            print("total users %d" % csvreader.line_num)
        # printing field names
        print('Field name are:' + ', '.join(field for field in fields))

        # printing first 5 rows
        print('\nFirst 5 rows are: \n')
        for row in rows[:3]:
            # parsing each coloumn of a row
            for col in row:
                print('%10s' % col, end=' '),
            print("\n")

# with open(filename, 'a') as self.deactivate:
#     print("entering into writing mode")
#     # create dictwrtier object
#     writer = csv.writer(self.deactivate)
# deactivate_user2 = csv.list_dialects()
# to write header.
# send_data_to_userinfo.writeheader()
# send_data_to_userinfo.writerow(self.user_data)
# print(f"\n user {self.first_name} has been added")
# for search in self.deactivate:
# if (search[-1]) == "active":
# changed_status = "inactive"
# deactivate_user[-1] = "inactive"
# writer = csv.writer(deactivate_user2)
# for key in writer:
#     key[-1] = "inactive"
#     writer.writerline([key[-1]],)

# deactivate_user.writerow()
