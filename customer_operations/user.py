import csv
from customer_operations.admin import Admin


class UserOperations(Admin):
    def __init__(self, send_amount, withdraw_amount, deposit_amount, transaction_time, current_balance, id_card,
                 is_admin, account_no, pin, first_name, last_name, father_name, dob, gender, email, age, user_data,
                 amount, status):
        super().__init__(is_admin, account_no, pin, first_name, last_name, father_name, dob, gender, email, age,
                         id_card, user_data, amount, status)

        self.send_amount = input("Enter Sending Amount:\t ")
        self.withdraw_amount = input("Enter Account no in digit:\t ")
        self.deposit_amount = input("Set pin in digits:\t ")
        self.transaction_time = input("Enter first name:\t ")
        self.current_balance = input("Enter last name:\t ")

        self.send_amount = send_amount
        self.withdraw_amount = withdraw_amount
        self.deposit_amount = deposit_amount
        self.transaction_time = transaction_time
        self.current_balance = current_balance

        self.user_transaction = {'send amount': self.send_amount, 'withdraw amount': self.withdraw_amount,
                                 'deposit amount': self.deposit_amount,
                                 'transaction time': self.transaction_time,
                                 'current balance': self.current_balance}

        filename = "user_data.csv"
        user_trans_file = "user_transaction.csv"


        print("please Enter User Credentials \t")
        user_pin = input("pin\t ")

        with open(filename, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            for i in data:
                if i[2] == user_pin:
                    print("User is Logged In\t ")
                    if i[0] == "no":
                        print(f"User {id_card} Welcome ")
                        with open(filename, "w", newline='') as fw:
                            fwriter = csv.writer(fw)
                            fwriter.writerows(data)
                        print(f"{id_card} data status changed to {i[12]} ")

        # open csv file
        # with open('transaction_data.csv', 'a', newline='') as self.userinfo:
        #     header = ['id_card', 'send amount', 'withdraw amount', 'deposit amount', 'transaction time',
        #               'current balance']
        #     send_data_to_userinfo = csv.DictWriter(self.userinfo, fieldnames=header)
        #     # to write header.
        #     send_data_to_userinfo.writeheader()
        #     # send_data_to_userinfo.writerow(self.user_data)
        #     # print(f"\n user {self.first_name} has been added")

        ########################################## operation deposit money #################################################

    def user_menu(self):
        filename = "user_data.csv"
        print("\t please Enter Admin Credentials")
        admin_card = input("\t Type ID card number without '-' ")
        print("\t Enter Account Pin")
        admin_pin = input("\t pin")

    def deposit_money(self):
        deposit_amount = int(input("please enter deposit amount"))
        print(f"you have deposited {deposit_amount} amount")

        file = open("deposit_data.txt", "a")
        line_id_deposit = str(line_id_received) + "," + str(deposit_amount) + "\n"
        file.write(line_id_deposit)
        file.close()

        # index = 0
        #
        # for line in file:
        #     index += 1
        #
        #     if line_id_received in file:
        #         print(line)
        #         print(f"this is your required line{deposit_amount}")

        print("your amount is saved")

        depositfile = open("deposit_data.txt", "r")
        namefile = open("customer_data.txt", "r")
        # file = open("customer_data_2.txt", 'w')
        # file.write(record)
        flag = 0
        index = 0

        for line in depositfile:
            index += 1
            line_id, amount = line.split(",")
            if str(line_id_received) == line_id:

                for namefind in namefile:
                    flag = flag + 1
                    name, password = namefind.split(",")

                    if str(flag) == str(line_id_received):
                        print(f"{name} have deposited pkr {amount}")
                        print("code for index check has been executed")
                        break
                    break

        print("for checking overall deposit amount ")
        chk_balance = input("enter 1")
        if chk_balance == "1":
            customer_operations.check_balance.chk_balance(line_id_received)
        print("code for index checking not executed")

        namefile.close()
        depositfile.close()


# ========================================================================================================================
########################### operation with draw money ###################################################################

def withdraw_balance(line_id_received):
    sums = 0
    withdraw_amount = input("please enter withdraw amount")
    depositfile = open("deposit_data.txt", "r")
    print("checking total amount")
    for total_amount_deposit in depositfile:
        print("in checking loop")
        line_id, amount = total_amount_deposit.split(",")
        if str(line_id_received) == line_id:
            sums = sums + int(amount)
            print(f"total money{sums}")

    remaining_balance = sums - int(withdraw_amount)
    # record_update = line_id_received + "," + "-" + withdraw_amount
    # depositfile.write(record_update)
    # depositfile.close()
    print(f"remaining balance {remaining_balance}")

    adjust_withdraw_amount = open("deposit_data.txt", "a")

    depositfile.close()


# ===============================================================================================================

# =====================operation check balance=======================
def chk_balance(line_id_received):
    sums = 0
    depositfile = open("deposit_data.txt", "r")
    print("checking total amount")
    for total_amount_deposit in depositfile:
        print("counting money you are rich")
        line_id, amount = total_amount_deposit.split(",")
        if str(line_id_received) == line_id:
            sums = sums + int(amount)
    print(f"total money{sums}")

    depositfile.close()
